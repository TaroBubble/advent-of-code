textFile = open('day5\input.txt', 'r')

def solution(textFile):
    arr = []
    res = []

    for line in textFile:
        arr.append(line.replace('\n', ''))

    for boardingpass in arr:
            row = boardingpass[:7].replace('F', '0')
            row = row.replace('B', '1')
            col = boardingpass[7:].replace('L', '0')
            col = col.replace('R', '1')
            resNum = (printBinary(row) * 8) + printBinary(col)
            res.append(resNum)
    return res

def printBinary(binaryNum):
    res = 0
    for num in binaryNum:
        res = res*2 + int(num)
    return int(res)

def solutionPart2(res):
    for i in range(min(res), max(res)+1):
        if i not in res:
            return i
    return None

print(solutionPart2(solution(textFile)))
