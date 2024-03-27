import sys
input = sys.stdin.readline

input_string = list(input())
number = ''
for_subtraction = []
answer = 0
minus = False

for string in input_string:
    if string in '0123456789':
        number += string
    elif string == '+':
        if not minus:
            answer += int(number)
            number = ''
        else:
            for_subtraction.append(int(number))
            number = ''
    elif string == '-':
        if not minus:
            minus = True
            answer += int(number)
        else:
            for_subtraction.append(int(number))
        number = ''

number = int(number)
if minus:
    for_subtraction.append(number)
else:
    answer += number

answer -= sum(for_subtraction)
print(answer)