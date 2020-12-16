def solution1():
    with open("input", "r") as f:
        treemap = []
        trees = 0
        for line in f.readlines():
            row = [None] * len(line)
            for i,c in enumerate(line):
                row[i] = c
            treemap.append(row[:-1])
    
        height = len(treemap)
        pattern = len(treemap[0])
        col = 0
        for i in range(height-1):
            col += 3
            if treemap[i+1][col%pattern] == "#":
                trees += 1
        return trees

def solution2():
    with open("input", "r") as f:
        treemap = []
        trees1 = 0
        trees3 = 0
        trees5 = 0
        trees7 = 0
        trees2 = 0
        for line in f.readlines():
            row = [None] * len(line)
            for i,c in enumerate(line):
                row[i] = c
            treemap.append(row[:-1])
    
        height = len(treemap)
        pattern = len(treemap[0])
        col1 = 0
        col3 = 0
        col5 = 0
        col7 = 0
        col2 = 0

        j = 0
        while j < height-1:
            col2 += 1
            if treemap[j+2][col2%pattern] == "#" and j+2 < height:
                trees2 += 1
            j += 2 


        for i in range(height-1):
            col1 += 1
            col3 += 3
            col5 += 5
            col7 += 7
            if treemap[i+1][col1%pattern] == "#":
                trees1 += 1
            if treemap[i+1][col3%pattern] == "#":
                trees3 += 1
            if treemap[i+1][col5%pattern] == "#":
                trees5 += 1
            if treemap[i+1][col7%pattern] == "#":
                trees7 += 1
        return trees1 * trees3 * trees5 * trees7 * trees2

print(solution1())
print(solution2())

