import re

def clearData(passport):
    return {}

def checkPassport1(passport):
    if len(passport.keys()) == 8:
        return True
    if len(passport.keys()) == 7 and "cid" not in passport.keys():
        return True
    return False

def checkPassport2(passport):
    if (len(passport.keys()) == 8 or
       (len(passport.keys()) == 7 and "cid" not in passport.keys())):
        return checkAllFields(passport)
    return False

def checkValidHeight(height):
    if height[-2:] == "cm":
        cm = int(height[:-2])
        return 150 <= cm <= 193
    if height[-2:] == "in":
        inch = int(height[:-2])
        return 59 <= inch <= 76

def checkAllFields(passport):
    byr = int(passport["byr"])
    iyr = int(passport["iyr"])
    eyr = int(passport["eyr"])
    
    
    hairColor = '^#[a-f0-9]{6}$'
    eyeColor = '^(amb|blu|brn|gry|grn|hzl|oth)$'
    pid = '^[0-9]{9}$'

    return (1920 <= byr <= 2002 and 2010 <= iyr <= 2020 and 2020 <= eyr <= 2030 and
       checkValidHeight(passport["hgt"]) and re.match(hairColor, passport["hcl"]) and
       re.match(eyeColor, passport["ecl"]) and re.match(pid, passport["pid"]))
       

def solution1():
    passport = {}
    numValid = 0
    with open("input", "r") as f:
        for line in f:
            if line != '\n':
                data = line.rstrip('\n')
                info = data.split(" ")
                for val in info:
                    item = val.split(":")
                    passport[item[0]] = item[1]
                
            else:
                if checkPassport1(passport):
                    numValid += 1
                passport = clearData(passport)
        return numValid

def solution2():
    passport = {}
    numValid = 0
    with open("input", "r") as f:
        for line in f:
            if line != '\n':
                data = line.rstrip('\n')
                info = data.split(" ")
                for val in info:
                    item = val.split(":")
                    passport[item[0]] = item[1]
                
            else:
                if checkPassport2(passport):
                    numValid += 1
                passport = clearData(passport)
        return numValid

print(solution1())
print(solution2())
