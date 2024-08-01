import sys
input = sys.stdin.readline

N = int(input())  # N: 퇴사 전 남은 일수

profits = [0 for _ in range(N + 1)]

schedule = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(i + schedule[i][0], N + 1):
        if profits[j] < profits[i] + schedule[i][1]:
            profits[j] = profits[i] + schedule[i][1]

print(profits[-1])