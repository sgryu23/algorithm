import sys
input = sys.stdin.readline

dp = [[0 for _ in range(3)] for i in range(100001)]
mod = 1000000009

dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for j in range(4, 100001):
    # 이전 수에서 2와 3으로 끝난 것에 1을 붙이기
    dp[j][0] = dp[j - 1][1] % mod + dp[j - 1][2] % mod
    # 2 개의 수 이전에서 1과 3으로 끝난 것에 2를 붙이기
    dp[j][1] = dp[j - 2][0] % mod + dp[j - 2][2] % mod
    # 3 개의 수 이전에서 1과 2로 끝난 거에 3을 붙이기
    dp[j][2] = dp[j - 3][0] % mod + dp[j - 3][1] % mod

t = int(input())

for test_case in range(t):
    n = int(input())
    print(sum(dp[n]) % mod)