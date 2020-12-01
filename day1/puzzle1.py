textFile = open("advent-of-code\day1\input.txt", "r")

numList = []
target = 2020

for line in textFile:
    numList.append(int(line.strip('\n')))

def solution(numList, target):
    numMap = {}
    for i in range(len(numList)):
        complement = target - numList[i]
        if complement in numMap:
            print(numMap)
            return (numList[i]*numList[numMap[complement]])
        else:
            numMap[numList[i]] = i
    return None

print(solution(numList, target))


