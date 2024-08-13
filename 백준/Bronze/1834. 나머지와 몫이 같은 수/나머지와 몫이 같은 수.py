import sys

N = int(sys.stdin.readline())
answer = 0

for i in range(1, N):
    answer += (N * i + i)

print(answer)