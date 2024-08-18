import sys

N, K = map(int, sys.stdin.readline().split())
mod = 10 ** 9

if K == 1:
    print(1)
else:
    dp = [[i for i in range(1, N + 2)]]
    for k in range(2, K):
        dp.append([0 for _ in range(N + 1)])
    for i in range(1, K - 1):
        dp[i][0] = 1
        for j in range(1, N + 1):
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % mod

    answer = dp[-1][-1] % mod
    print(answer)