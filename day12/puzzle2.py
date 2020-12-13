textFile = open('day12\input.txt', 'r')

arr = []

for line in textFile:
    line = line.strip()
    arr.append([line[0], line[1:]])

print(arr)

def solution(data):
    x = 0
    y = 0
    wayX = 10
    wayY = 1

    for i in range(len(data)):
        distance = int(data[i][1])
        if data[i][0] == 'E':
            wayX += distance
        elif data[i][0] == 'W':
            wayX -= distance
        elif data[i][0] == 'N':
            wayY += distance
        elif data[i][0] == 'S':
            wayY -= distance
        elif data[i][0] == 'R':
            if distance == 90:
                wayX, wayY = wayY, -wayX
            elif distance == 180:
                wayX, wayY = -wayX, -wayY
            elif distance == 270:
                wayX, wayY = -wayY, wayX
        elif data[i][0] == 'L':
            if distance == 90:
                wayX, wayY = -wayY, wayX
            elif distance == 180:
                wayX, wayY = -wayX, -wayY
            elif distance == 270:
                wayX, wayY = wayY, -wayX
        elif data[i][0] == 'F':
            x += distance * wayX
            y += distance * wayY
    return abs(x) + abs(y)

print(solution(arr))