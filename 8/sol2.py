# not mine

file = open("input").read().splitlines()

instructions = []

for line in file:
    instructions.append((line.split(" ")[0], int(line.split(" ")[1].replace("+", ""))))


def terminates(list):
    cur = 0
    acc = 0
    visited = set()
    while cur != len(list):
        if visited.__contains__(cur):
            return False
        else:
            visited.add(cur)
        if list[cur][0] == "acc":
            acc += list[cur][1]; cur += 1
        elif list[cur][0] == "jmp":
            cur += list[cur][1];
        else:
            cur += 1
    print(acc)
    return True


for i, instruction in enumerate(instructions):
    if instruction[0] == "acc": continue
    if instruction[0] == "nop":
        instructions[i] = ("jmp", instruction[1])
    else:
        instructions[i] = ("nop", instruction[1])
    if terminates(instructions): break;
    if instruction[0] == "nop":
        instructions[i] = ("nop", instruction[1])
    else:
        instructions[i] = ("jmp", instruction[1])
