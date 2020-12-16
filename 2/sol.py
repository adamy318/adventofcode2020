#!/bin/bash



def solution1():
    solution = 0
    with open("input", "r") as f:
        for line in f.readlines():
            data = line.split(" ")
            numbers = data[0].split("-")
            least = int(numbers[0])
            highest = int(numbers[1])
            letter = data[1][0]
            password = data[2]
            count = password.count(letter)
            if least <= count <= highest:
                solution += 1

    return solution
            

def solution2():
    solution = 0
    with open("input", "r") as f:
        for line in f.readlines():
            data = line.split(" ")
            numbers = data[0].split("-")
            index1 = int(numbers[0])-1
            index2 = int(numbers[1])-1
            letter = data[1][0]
            password = data[2]
            if password[index1] == letter:
                if password[index2] != letter:
                    solution += 1
            else:
                if password[index2] == letter:
                    solution += 1

    return solution

print(solution1())
print(solution2())
