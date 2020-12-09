textFile = open('day8\input.txt', 'r')

code = []

for line in textFile:
    line = line.strip()
    operation = line[:3]
    value = line[4:]
    code.append([operation, value])


def solution(codeArr):
    accumulator = 0
    item = 0
    ranInstruction = []
    while item not in ranInstruction:
        operation = codeArr[item]
        if operation[0] == 'nop':
            ranInstruction.append(item)
            item += 1

        elif operation[0] == 'acc':
            ranInstruction.append(item)
            accumulator += int(operation[1])
            item += 1
            
        elif operation[0] == 'jmp':
            ranInstruction.append(item)
            item += int(operation[1])
            
    return accumulator

print(solution(code))