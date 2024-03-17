import sys
input = sys.stdin.readline

n = int(input())  # n: 포도주 잔의 개수
wines = [0] * 10000
for i in range(n):
    wines[i] = int(input())

dp = [0 for _ in range(10000)]
dp[0] = wines[0]
dp[1] = wines[0] + wines[1]
dp[2] = max(wines[0] + wines[2], wines[1] + wines[2], dp[1])
for j in range(3, n):
    dp[j] = max(wines[j] + dp[j - 2], wines[j] + wines[j - 1] + dp[j - 3], dp[j - 1])

print(max(dp))