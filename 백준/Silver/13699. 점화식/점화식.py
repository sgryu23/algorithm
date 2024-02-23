import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(36)]

dp[0] = 1
dp[1] = 1
for i in range(2, 36):
    for k in range(0, i):
        dp[i] += dp[k] * dp[i - 1 - k]

print(dp[n])