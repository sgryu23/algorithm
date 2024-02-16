import sys
input = sys.stdin.readline

n = int(input())
mod = 9901
dp = [0 for _ in range(n + 1)]
dp[1] = 3
if n > 1:
    dp[2] = 7
if n > 2:
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] * 2 + dp[i - 2]) % mod
print(dp[n] % mod)