import re

textFile = open("day4\input.txt", "r")

def solution(textFile):
    byr = iyr = eyr = hgt = hcl = ecl = pid = False
    res = 0
    fieldDict = dict()
    fields = []
    delim = ':'
    for line in textFile:
        dicts = line.split()
        for field in dicts:
            fieldDict[field.split(delim)[0]] = field.split(delim)[1]

        if not line.strip():

            if 'byr' in fieldDict:
                byrVal = fieldDict['byr']
                if 1920 <= int(byrVal) <= 2002:
                    byr = True

            if 'iyr' in fieldDict:
                iyrVal = fieldDict['iyr']
                if 2010 <= int(iyrVal) <= 2020:
                    iyr = True

            if 'eyr' in fieldDict:
                eyrVal = fieldDict['eyr']
                if 2020 <= int(eyrVal) <= 2030:
                    eyr = True

            if 'hgt' in fieldDict:
                hgtVal = fieldDict['hgt']
                if 'cm' in hgtVal:
                    hgtVal = hgtVal.replace('cm', '')
                    if 150 <= int(hgtVal) <= 193:
                        hgt = True
                elif 'in' in hgtVal:
                    hgtVal = hgtVal.replace('in', '')
                    if 59 <= int(hgtVal) <= 76:
                        hgt = True

            if 'hcl' in fieldDict:
                hclVal = fieldDict['hcl']
                if re.fullmatch('#([0-9]|[a-f]){6}', hclVal):
                    hcl = True

            if 'ecl' in fieldDict:
                eclVal = fieldDict['ecl']
                if re.fullmatch('amb|blu|brn|gry|grn|hzl|oth', eclVal):
                    ecl = True

            if 'pid' in fieldDict:
                pidVal = fieldDict['pid']
                if re.fullmatch('[0-9]{9}', pidVal):
                    pid = True     
            if byr and iyr and eyr and hgt and hcl and ecl and pid:
                res += 1
            byr = iyr = eyr = hgt = hcl = ecl = pid = cid = False 
            fieldDict.clear()
    return res
 
print(solution(textFile))
