textFile = open('day13/input.txt', 'r')
textFile = textFile.read().split('\n')
textFile = textFile[1].split(',')
arr = []

for i in range(len(textFile)):
    if textFile[i] != 'x':
        arr.append((int(textFile[i]), i))
print(arr)

def solution(arr):
    time = 0
    num = 1
    for i in range(len(arr)-1):
        bus = arr[i+1][0]
        busTime = arr[i+1][1]
        num *= arr[i][0]
        while (time + busTime) % bus != 0:
            time += num
    return time

print(solution(arr))