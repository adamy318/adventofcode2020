def convertToNumber(code):
    binary =  bin(int(''.join(map(str, code)), 2)) 
    return int(binary, 2)

def solution1():
    maxSeatID = 0
    with open("input", "r") as f:
        for line in f:
            rowBin = []
            colBin = []

            for i in range(7):
                if line[i] == "F":
                    rowBin.append(0)
                elif line[i] == "B":
                    rowBin.append(1)

            for j in range(7,10):
                if line[j] == "L":
                    colBin.append(0)
                elif line[j] == "R":
                    colBin.append(1)

            row = convertToNumber(rowBin)
            col = convertToNumber(colBin)
            seatID = (row * 8) + col
            maxSeatID = max(maxSeatID, seatID)

    return maxSeatID

def solution2():
    seats = []
    mySeat = 0
    with open("input", "r") as f:
        for line in f:
            rowBin = []
            colBin = []

            for i in range(7):
                if line[i] == "F":
                    rowBin.append(0)
                elif line[i] == "B":
                    rowBin.append(1)

            for j in range(7,10):
                if line[j] == "L":
                    colBin.append(0)
                elif line[j] == "R":
                    colBin.append(1)

            row = convertToNumber(rowBin)
            col = convertToNumber(colBin)
            seatID = (row * 8) + col
            seats.append(seatID)

    sortedSeats = sorted(seats)
    for i in range(len(sortedSeats)-1):
        if sortedSeats[i]+1 != sortedSeats[i+1]:
            mySeat = sortedSeats[i]+1
            break
    return mySeat


print(solution1())
print(solution2())
