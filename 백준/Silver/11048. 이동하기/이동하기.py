import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [[0 for _ in range(M)] for r in range(N)]

dp[0][0] = arr[0][0]

for c in range(1, M):
    dp[0][c] = dp[0][c - 1] + arr[0][c]

for r in range(1, N):
    dp[r][0] = dp[r - 1][0] + arr[r][0]

for row in range(1, N):
    for col in range(1, M):
        dp[row][col] = arr[row][col] + max(dp[row - 1][col], dp[row - 1][col - 1], dp[row][col - 1])

print(dp[-1][-1])