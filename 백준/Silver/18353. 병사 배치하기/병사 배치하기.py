import sys
input = sys.stdin.readline

N = int(input())  # N: qudtkdml tn
soldiers = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if soldiers[j] > soldiers[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))