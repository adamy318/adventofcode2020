def checkValid(window, target):
    for i in range(len(window)-1):
        for j in range(i+1,len(window)):
            if window[i]+window[j] == target:
                return True
    return False

def getNumbers():
    numbers = []
    with open("input", "r") as f:
        for line in f:
            numbers.append(int(line.rstrip()))
    return numbers


def solution1():
    numbers = getNumbers()

    badNumber = 0
    windowSize = 25
    for i in range(len(numbers)-(windowSize)):
        if not checkValid(numbers[i:i+windowSize],numbers[i+windowSize]):
            badNumber = numbers[i+windowSize]
    return badNumber

def solution2():
    numbers = getNumbers()
    badNumber = solution1()

    start = 0
    end = 0
    longest = []
    runningTotal = numbers[0]
    while end < len(numbers)-1:
        if runningTotal < badNumber:
            end += 1
            runningTotal += numbers[end]
        elif runningTotal == badNumber:
            if len(numbers[start:end]) > len(longest):
                longest = numbers[start:end]
            runningTotal -= numbers[start]
            start += 1
            end += 1
            runningTotal += numbers[end]
        else:
            runningTotal -= numbers[start]
            start += 1

    return min(longest) + max(longest)


print(solution1())
print(solution2())
