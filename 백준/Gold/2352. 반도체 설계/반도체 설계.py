import sys
input = sys.stdin.readline

n = int(input())
ports = list(map(int, input().split()))
dp = [0 for _ in range(n)]

for i in range(n):
    dp[i] = 1
    for j in range(i):
        if ports[i] > ports[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))