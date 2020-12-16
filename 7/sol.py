import re

rules = []
rules2 = []

def findParentBags(color, data):
    global rules
    pattern = ".*"+color+".+"
    parentBags = 0
    bagCount = 0
    for line in data:
        match = re.search(pattern, line.rstrip('\n'))
        if match:

            if match[0] in rules:
                continue

            rule = match[0].split()
            firstColor = rule[0]+" "+rule[1]

            if firstColor == color:
                continue
            else:
                bagCount += 1
                rules.append(match[0])
                parentBags += findParentBags(firstColor, data)

    return bagCount + parentBags

def findChildBags(color, data, totalBags):
    global rules2
    rulePattern = "^"+color+".+"
    bagPattern = "(?!^)([0-9] \w+ \w+ bags*)+"

    colors = []
    bags = 0
    allChildren = 0

    for line in data:
        match = re.search(rulePattern, line.rstrip())
        if match:
            if match[0] not in rules2:
                rules2.append(match[0])

            for bag in re.findall(bagPattern, match[0]):

                bagNumber = int(bag[0])
                bags += bagNumber 
                totalBags *= bagNumber

                bagSplit = bag.split()
                bagColor = bagSplit[1]+" "+bagSplit[2]
                allChildren += bagNumber*findChildBags(bagColor, data, totalBags)
    return bags + allChildren

def solution1():

    data = []
    with open("input", "r") as f:
        for line in f:
            data.append(line.rstrip())
    return findParentBags("shiny gold", data)

def solution2():

    data = []
    with open("input", "r") as f:
        for line in f:
            data.append(line.rstrip())
    return findChildBags("shiny gold", data, 1)

print(solution1())
print(solution2())
