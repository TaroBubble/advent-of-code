textFile = open('day7\input.txt', 'r')

rules = dict()

for line in textFile:
    val = []
    if 'no' in line:
        line = line.strip().split(' contain ')
        line[0] = line[0].replace(' bags', '')
        value = line[1].replace(' bags','').replace(' bag','').replace('.','')
        rules[line[0]] = [value]
    else:
        line = line.strip().split(' contain ')
        line[0] = line[0].replace(' bags', '')
        value = line[1].replace(' bags','').replace(' bag','').replace('.','')
        value = value.split(', ')
        for item in value:
            num = item[0]
            color = item[2:]
            val += [[int(num), color]]
        rules[line[0]] = val

def checkDict(key, isChecked):
    for item in rules[key]:
        if 'shiny gold' in item:
            return 1
        if 'no other' in item:
            return 0

    for item in rules[key]:
        isChecked += checkDict(item[1], isChecked)

    if isChecked:
        return 1
    else:
        return 0

def solution(rules):
    res = 0
    for key in rules:
        if checkDict(key, 0):
            res += 1
    return res

print(solution(rules))