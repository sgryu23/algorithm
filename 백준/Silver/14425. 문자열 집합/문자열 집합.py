import sys
input = sys.stdin.readline

N, M = map(int, input().split())

sets = set()
answer = 0

for _ in range(N):
    sets.add(input())

for i in range(M):
    if input() in sets:
        answer += 1

print(answer)