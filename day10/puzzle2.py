from collections import defaultdict

textFile = open('day10\input.txt', 'r')

data = []

for line in textFile:
    line = line.strip()
    data.append(int(line))

data.sort()

def solution(arr):
    res = defaultdict(int)
    res[0] = 1
    for item in arr:
        res[item] = res[item-1] + res[item-2] + res[item-3]
    return res[max(arr)]

print(solution(data))