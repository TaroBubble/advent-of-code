textFile = open("day3\input.txt", "r")

puzzle = []

for line in textFile.read().split():
    puzzle.append(line)

right = 3
down = 1

def solution(puzzle, right, down):
    pos = 0
    widthOfPuzzle = len(puzzle[0])
    depthOfPuzzle = len(puzzle)
    res = 0
    for i in range(0, depthOfPuzzle, down):
        if puzzle[i][pos] == "#":
            res += 1
        pos = (pos+right) % widthOfPuzzle
    return res

print(solution(puzzle, right, down))