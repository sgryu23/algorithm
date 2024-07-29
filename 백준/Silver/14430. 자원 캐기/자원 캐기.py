import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # N: 세로 길이, M: 가로 길이

arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [[0 for c in range(M)] for r in range(N)]

dp[0][0] = arr[0][0]

for i in range(1, M):
    dp[0][i] = arr[0][i] + dp[0][i - 1]

for j in range(1, N):
    dp[j][0] = arr[j][0] + dp[j - 1][0]

for row in range(1, N):
    for col in range(1, M):
        dp[row][col] = max(dp[row - 1][col] + arr[row][col], dp[row][col - 1] + arr[row][col])

print(dp[-1][-1])