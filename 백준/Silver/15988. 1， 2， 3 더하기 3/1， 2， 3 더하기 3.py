import sys
input = sys.stdin.readline

t = int(input())
mod = 1000000009
dp = [0 for _ in range(1000001)]
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 1000001):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % mod

for tc in range(t):
    n = int(input())
    print(dp[n])