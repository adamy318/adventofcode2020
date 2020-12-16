#!/usr/bin/python3

with open("input", "r") as fin, open("output", "w") as fout:
    for line in fin.readlines():
        if line == '\n':
            continue
        else:
            fout.write(line)
