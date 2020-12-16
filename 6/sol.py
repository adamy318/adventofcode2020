def clearData(data):
    data = {}
    return data

def solution1():
    sumOfYes = 0
    questions = {}
    with open("input", "r") as f:
        for line in f:
            if line != '\n':
                for person in line.rstrip('\n'):
                    if person not in questions:
                        questions[person] = 1
                    else:
                        questions[person] += 1

            else:
                sumOfYes += len(questions.keys())
                questions = clearData(questions)
    return sumOfYes

def solution2():
    sumOfAll = 0
    allPeople = 0
    questions = {}
    with open("input", "r") as f:
        for line in f:
            if line != '\n':
                for person in line.rstrip('\n'):
                    if person not in questions:
                        questions[person] = 1
                    else:
                        questions[person] += 1
                allPeople += 1

            else:
                yes = [x for x in questions.values() if x == allPeople]
                sumOfAll += len(yes)
                questions = clearData(questions)
                allPeople = 0
    return sumOfAll

print(solution1())
print(solution2())
