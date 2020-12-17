def getInstructions():
    instructions = {}
    with open("input", "r") as f:
        for i,line in enumerate(f):
            instructions[i] = line.rstrip()
    return instructions


def solution1():
    count = {}
    allInstruct = []
    instructions = getInstructions()

    for i in range(len(instructions)):
        count[i] = 0

    i = 0
    acc = 0
    while 1:
        allInstruct.append((i,instructions[i]))
        inSplit = instructions[i].split()
        instruction = inSplit[0]
        operand = inSplit[1]

        if instruction == "acc":
            if operand[0] == "+":
                acc += int(operand[1:])
            elif operand[0] == "-":
                acc -= int(operand[1:])
            i += 1

        elif instruction == "nop":
            i += 1

        elif instruction == "jmp":
            if operand[0] == "+":
                i += int(operand[1:])
            elif operand[0] == "-":
                i -= int(operand[1:])
        count[i] += 1
        if count[i] == 2:
            break
    return acc, allInstruct

def fixCorruptInstruction(instructions, corrupt):
    instr = corrupt[1].split()
    corruptInstr = instr[0]
    corruptOperand = instr[1]

    print("corrupt: ",corrupt)
    if corruptInstr == "jmp":
        instructions[corrupt[0]] = "nop"+" "+corruptOperand
    elif corruptInstr == "nop":
        instructions[corrupt[0]] = "jmp"+" "+corruptOperand

    return instructions

def checkInfLoop(instructions):
    count = {}

    for i in range(len(instructions)):
        count[i] = 0

    i = 0
    while i < len(instructions):
        inSplit = instructions[i].split()
        instruction = inSplit[0]
        operand = inSplit[1]

        if instruction == "acc":
            i += 1

        elif instruction == "nop":
            i += 1

        elif instruction == "jmp":
            if operand[0] == "+":
                i += int(operand[1:])
            elif operand[0] == "-":
                i -= int(operand[1:])
        if i >= len(instructions):
            break
        count[i] += 1
        if count[i] == 2:
            return True
    return False


def solution2():
    instructions = getInstructions()

    i = 0
    acc = 0

    for ins in range(len(instructions)):
        fixedInstructions = fixCorruptInstruction(instructions, (ins,instructions[ins]))
        if not checkInfLoop(fixedInstructions):
            print(ins, fixedInstructions[ins])
            while i < len(fixedInstructions):
                inSplit = fixedInstructions[i].split()
                instruction = inSplit[0]
                operand = inSplit[1]

                if instruction == "acc":
                    if operand[0] == "+":
                        acc += int(operand[1:])
                    elif operand[0] == "-":
                        acc -= int(operand[1:])
                    i += 1

                elif instruction == "nop":
                    i += 1

                elif instruction == "jmp":
                    if operand[0] == "+":
                        i += int(operand[1:])
                    elif operand[0] == "-":
                        i -= int(operand[1:])
            break
    return acc



print(solution1()[0])
#print(solution1()[1])
print(solution2())
