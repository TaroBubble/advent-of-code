textFile = open("advent-of-code\day1\input.txt", "r")

numList = []
target = 2020

for line in textFile:
    numList.append(int(line.strip('\n')))

def solution(numList, target):
    numList.sort()
    for i in range(len(numList)-2):
        if numList[i] == numList[i-1] and i > 0:
            continue
        left = i+1
        right = len(numList)-1
        while left < right:
            sumNum = numList[i] + numList[left] + numList[right]
            if sumNum == target:
                return numList[i]*numList[left]*numList[right]
            elif sumNum > 0:
                right -= 1
            else:
                left += 1
    return None

print(solution(numList, target))