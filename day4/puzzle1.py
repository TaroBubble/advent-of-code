textFile = open("day4\input.txt", "r")


def solution(textFile):
    byr = iyr = eyr = hgt = hcl = ecl = pid = False
    res = 0

    for line in textFile:

        if 'byr' in line:
            byr = True
        if 'iyr' in line:
            iyr = True
        if 'eyr' in line:
            eyr = True
        if 'hgt' in line:
            hgt = True
        if 'hcl' in line:
            hcl = True
        if 'ecl' in line:
            ecl = True
        if 'pid' in line:
            pid = True
        if 'cid' in line:
            cid = True

        if not line.strip():
            if byr and iyr and eyr and hgt and hcl and ecl and pid:
                res += 1
            byr = iyr = eyr = hgt = hcl = ecl = pid = cid = False

    return res

print(solution(textFile))