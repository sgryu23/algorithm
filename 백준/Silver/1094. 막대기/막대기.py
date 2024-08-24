import sys
X = int(sys.stdin.readline())

power = 6
answer = 0

while X > 0:
    if X - (2 ** power) < 0:
        power -= 1
    else:
        X -= 2 ** power
        power -= 1
        answer += 1

print(answer)