textFile = open('day8\input.txt', 'r')

code = []

for line in textFile:
    line = line.strip()
    operation = line[:3]
    value = line[4:]
    code.append([operation, value])

def part1(codeArr):
    item = 0
    accumulator = 0
    ranInstruction = []

    while item not in ranInstruction:
        operation = codeArr[item]
        num = int(operation[1])

        if operation[0] == 'nop':
            ranInstruction.append(item)
            item += 1

        elif operation[0] == 'acc':
            accumulator += num
            ranInstruction.append(item)
            item += 1

        elif operation[0] == 'jmp':
            ranInstruction.append(item)
            item += num

        if item == len(codeArr):
            return (True, accumulator)

    return (False, accumulator)

def solution(code):
    notLooped = None
    for i in range(len(code)):
        nope = code[i][0] == 'nop'
        jump = code[i][0] == 'jmp'

        if nope or jump:
            copy = code.copy()

            if jump:
                copy[i] = ['nop', code[i][1]]
                notLooped = part1(copy)
                
            if nope:
                copy[i] = ['jmp', code[i][1]]
                notLooped = part1(copy)

            if notLooped[0] == True:
                return notLooped
    
print(solution(code))