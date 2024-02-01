import sys
input = sys.stdin.readline

n = int(input())
dp = [1] * (n + 1)
if n >= 2:
    for i in range(2, n + 1):
        dp[i] += (dp[i - 2] + dp[i - 1])

print(dp[n] % 1000000007)