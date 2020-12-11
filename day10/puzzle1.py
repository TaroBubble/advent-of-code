textFile = open('day10\input.txt', 'r')

data = []

for line in textFile:
    line = line.strip()
    data.append(int(line))

data.sort()

def solution(arr):
    count1 = 0
    count3 = 0
    prev = 0
    difference = 0
    for i in range(1, len(arr)):
        difference = arr[i] - arr[prev]
        if difference == 3:
            count3 += 1
        if difference == 1:
            count1 += 1
        prev += 1
    count1 += 1
    count3 += 1
    return count1, count3, count1*count3

print(solution(data))