import sys
input = sys.stdin.readline

n = int(input())
answer = 0

for _ in range(n):
    answer += int(input())

print(answer)