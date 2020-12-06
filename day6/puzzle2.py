textFile = open('day6\input.txt', 'r')

def solution(textFile):
    res = 0
    answerGroup = textFile.read().split('\n\n')

    for item in answerGroup:
        solutionSet = set()
        solutionSet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
        for answer in item.split():
            solutionSet = solutionSet.intersection(set(answer))
        res += len(solutionSet)

    return res

print(solution(textFile))