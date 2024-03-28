import sys
input = sys.stdin.readline

mod = 1000000000
N = int(input())  # N: 자리 수
dp = [[0 for c in range(10)] for r in range(N + 1)]

for i in range(1, 10):
    dp[1][i] = 1

for j in range(2, N + 1):
    for k in range(10):
        if k == 0:
            dp[j][k] = dp[j - 1][1]
        elif k == 9:
            dp[j][k] = dp[j - 1][8]
        else:
            dp[j][k] = dp[j - 1][k - 1] + dp[j - 1][k + 1]

print(sum(dp[N]) % mod)