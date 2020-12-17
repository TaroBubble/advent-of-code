textFile = open('day13/input.txt', 'r')

arr = []

for line in textFile:
    line = line.strip()
    if 'x' not in line:
        arr.append(int(line))
    else:
        line = line.replace('x,', '')
        line = line.split(',')
        for item in line:
            arr.append(int(item))

def solution(arr):
    res = []
    depTime = arr[0]
    for i in range(1,len(arr)):
        remainder = depTime % arr[i]
        res.append(remainder)
    arr.remove(depTime)
    difference = []
    for i in range(len(res)):
        diff = arr[i] - res[i]
        difference.append(diff)
    minWait = min(difference)
    index = difference.index(minWait)
    return minWait * arr[index]

print(solution(arr))