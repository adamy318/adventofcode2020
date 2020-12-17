import sys
import resource
import functools

class recursionlimit:

    def __init__(self, limit):
        self.limit = limit
        self.old_limit = sys.getrecursionlimit()
        self.old_rlimit = resource.getrlimit(resource.RLIMIT_STACK)

    def __enter__(self):

        sys.setrecursionlimit(self.limit)
        resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])

    def __exit__(self, type, value, tb):
        sys.setrecursionlimit(self.old_limit)
        resource.setrlimit(resource.RLIMIT_STACK, self.old_rlimit)

def solution1():
    adapters = []
    with open("input", "r") as f:
        for line in f:
            adapters.append(int(line.rstrip()))
    adapters = sorted(adapters)

    onediff = 0
    threediff = 0
    prevAdapter = 0
    for adapter in adapters:
        diff = adapter - prevAdapter
        if diff == 1:
            onediff += 1
        elif diff == 3:
            threediff += 1
        prevAdapter = adapter
    threediff += 1
    return onediff * threediff

def findAdapterCombos(adapters):

    @functools.lru_cache()
    def backtrack(index,adapters, curr, prevAdapter):

        if index >= len(adapters):
            if sorted(curr)[-1] == adapters[-1]:
                if sorted(curr) not in allCombos:
                    allCombos.append(curr[:])
            return

        for i in range(index,len(adapters)):

            if adapters[i] - prevAdapter > 3:
                return
            if adapters[i] - prevAdapter == 1:
                curr.append(adapters[i])
                backtrack(index+1, adapters, curr, adapters[i])
                backtrack(index+2, adapters, curr, adapters[i])
                backtrack(index+3, adapters, curr, adapters[i])
                curr.pop()
            if adapters[i] - prevAdapter == 2:
                curr.append(adapters[i])
                backtrack(index+1, adapters, curr, adapters[i])
                backtrack(index+2, adapters, curr, adapters[i])
                curr.pop()

            if adapters[i] - prevAdapter == 3:
                curr.append(adapters[i])
                backtrack(index+1, adapters, curr, adapters[i])
                curr.pop()


    allCombos = []
    
    backtrack(1, tuple(adapters), tuple([0]), 0)

    return len(allCombos)


def solution2():
    adapters = []
    with open("input", "r") as f:
        for line in f:
            adapters.append(int(line.rstrip()))
    adapters = sorted(adapters)
    adapters.insert(0,0)
    adapters.append(adapters[-1]+3)

    with recursionlimit(0x100000):
        return findAdapterCombos(adapters)



print(solution1())
print(solution2())
