import sys
input = sys.stdin.readline
while True:
    N = int(input())
    if N == 0:
        quit()

    dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

    for i in range(1, N + 1):
        dp[i][1] = 1
        dp[1][i] = 1

    for i in range(2, N + 1):
        for j in range(2, N + 1):
            if i >= j:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            else:
                dp[i][j] = dp[i][i]

    print(dp[N][N])