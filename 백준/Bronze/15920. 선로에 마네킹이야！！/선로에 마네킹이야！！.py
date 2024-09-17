import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()

lever = False
section = 0

for i in S:
    if i == 'P':
        if section == 1:
            answer = 6
        lever = not lever
    else:
        if section == 0:
            if lever:
                answer = 1
            else:
                answer = 5
        section += 1

if section >= 2:
    print(answer)
else:
    print(0)