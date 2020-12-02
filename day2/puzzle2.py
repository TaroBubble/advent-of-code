textFile = open("day2\input.txt", "r")

def solution(textFile):
    res = 0
    pos1Match = False
    pos2Match = False
    for line in textFile:
        newLine = line.replace(":", "").replace("\n","").replace("-", " ")
        pos1, pos2, letter, passWord = newLine.split()
        pos1 = int(pos1) - 1
        pos2 = int(pos2) - 1
        if passWord[pos1] == letter or passWord[pos2] == letter:
            if passWord[pos1] == letter:
                pos1Match = True
            if passWord[pos2] == letter:
                pos2Match = True
        print(pos1Match, pos2Match)
        if (pos1Match == 1 and pos2Match == 0) or (pos1Match == 0 and pos2Match == 1):
            res += 1
        pos1Match = False
        pos2Match = False
    return res
        
print(solution(textFile))