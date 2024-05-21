import sys

N = int(sys.stdin.readline())

dp = [1 for _ in range(10)]
div_num = 10007

for i in range(1, N):
    for j in range(1, 10):
        dp[j] += dp[j - 1]

answer = sum(dp) % div_num

print(answer)