textFile = open('day6\input.txt', 'r')

def solution(textFile):
    res = 0
    solutionSet = set()

    for line in textFile:
        line = line.strip()
        if line:
            for char in line:
                solutionSet.add(char)

        if not line:
            res += len(solutionSet)
            solutionSet.clear()

    return res + len(solutionSet)

print(solution(textFile))