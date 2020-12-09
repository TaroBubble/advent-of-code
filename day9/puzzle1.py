textFile = open('day9\input.txt', 'r')

data = []
res = []

for line in textFile:
    line = line.strip()
    data.append(line)

def bubble(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            sumNum = int(arr[i]) + int(arr[j])
            if sumNum == int(target):
                return 0
    res.append(target)
    return 0
            
def solution(data):
    num = []
    for i in range(25, len(data)):
        left = i-25
        sumVal = 0
        while left <= i:
            leftData = int(data[left])
            if leftData < int(data[i]):
                num.append(leftData)
            left += 1
        bubble(num, data[i])
        num.clear()
    return int(res[0])
        
print(solution(data))