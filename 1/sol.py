#!/bin/python3

def solution():
    target = 2020
    solution = 0
    data = []
    with open("input", "r") as f:
        for line in f.readlines():
            data.append(int(line.strip()))
    
    for i in range(len(data)-2):
        for j in range(i+1,len(data)-1):
            for k in range(i+2,len(data)):
                if data[i]+data[j]+data[k] == target:
                    solution = data[i]*data[j]*data[k]
                    return solution

def main():
    print(solution())
main()
