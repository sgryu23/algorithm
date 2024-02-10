import sys
input = sys.stdin.readline

n = int(input())
balls = list(input())

find_blue = False
answer_red = 0
for ball in range(n, -1, -1):
    if balls[ball] == 'B' and not find_blue:
        find_blue = True
    elif balls[ball] == 'R' and find_blue:
        answer_red += 1

find_red = False
answer_blue = 0
for ball in range(n, -1, -1):
    if balls[ball] == 'R' and not find_red:
        find_red = True
    elif balls[ball] == 'B' and find_red:
        answer_blue += 1

answer = min(answer_red, answer_blue)
print(answer)