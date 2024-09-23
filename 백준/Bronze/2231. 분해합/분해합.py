import sys
input = sys.stdin.readline

N = int(input())

answer = 0
number = 1

while number <= N:
    cand = []
    for c in str(number):
        cand.append(int(c))
    if sum(cand) + number == N:
        answer = number
        break
    number += 1

print(answer)