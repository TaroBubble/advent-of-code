textFile = open("day3\input.txt", "r")

puzzle = []

for line in textFile.read().split():
    puzzle.append(line)

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

slope1 = solution(puzzle, 1, 1)
slope2 = solution(puzzle, 3, 1)
slope3 = solution(puzzle, 5, 1)
slope4 = solution(puzzle, 7, 1)
slope5 = solution(puzzle, 1, 2)

print(slope1, slope2, slope3, slope4, slope5)
print(slope1*slope2*slope3*slope4*slope5)