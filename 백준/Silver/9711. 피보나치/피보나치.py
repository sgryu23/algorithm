import sys
input = sys.stdin.readline

t = int(input())
dp = [0] * 10001
dp[1] = 1
dp[2] = 1
for i in range(3, 10001):
    dp[i] += dp[i - 1] + dp[i - 2]

for tc in range(1, t + 1):
    p, q = map(int, input().split())
    ans = dp[p] % q
    print(f'Case #{tc}: {ans}')