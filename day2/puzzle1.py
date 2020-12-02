textFile = open("day2\input.txt", "r")

def solution(textFile):
    res = 0
    for line in textFile:
        newLine = line.replace(":", "").replace("\n","").replace("-", " ")
        low, high, letter, passWord = newLine.split()
        numLetterInPass = passWord.count(letter)
        if int(low) <= numLetterInPass <= int(high):
            res += 1
    return res
        

print(solution(textFile))