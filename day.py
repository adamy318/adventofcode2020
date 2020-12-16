#!/usr/bin/python3

import sys, os

if len(sys.argv) < 2:
    print("please give one number for day you want.")
    sys.exit(1)
if len(sys.argv) > 2:
    print("please give only one number for day you want.")
    sys.exit(1)

directory = str(sys.argv[1])
parent_dir = "/home/adam/adventofcode"
path = os.path.join(parent_dir, directory)

os.mkdir(path)
print("directory for day %s created", directory)

input_path = os.path.join(path, "input")
sol_path = os.path.join(path, "sol.py")

os.mknod(input_path)
os.mknod(sol_path)
