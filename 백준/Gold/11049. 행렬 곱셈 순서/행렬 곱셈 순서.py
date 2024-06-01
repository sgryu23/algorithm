import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for c in range(N)] for r in range(N)]

for i in range(1, N):
    for j in range(N):
        # 범위를 벗어나는 건 무시
        if i + j == N:
            break

        dp[j][i + j] = 2 ** 31

        for k in range(j, j + i):
            dp[j][j + i] = min(dp[j][j + i], dp[j][k] + dp[k + 1][j + i] + arr[j][0] * arr[k][1] * arr[j + i][1])

print(dp[0][N - 1])