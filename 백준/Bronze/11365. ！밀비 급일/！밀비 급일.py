import sys
input = sys.stdin.readline

while True:
    input_string = input().rstrip()
    if input_string == 'END':
        break
    stack = []
    for s in input_string:
        stack.append(s)

    answer = ''
    while stack:
        answer += stack.pop()

    print(answer)