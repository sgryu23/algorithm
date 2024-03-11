import sys
input = sys.stdin.readline

T = int(input())  # T: 테스트 케이스 개수
dp = [[0 for i in range(30)] for j in range(30)]

for r in range(30):
    for c in range(30):
        if r == 1:
            dp[r][c] = c
        else:
            if r == c:
                dp[r][c] = 1
            elif r < c:
                dp[r][c] = dp[r - 1][c - 1] + dp[r][c - 1]

for test_case in range(T):
    west, east = map(int, input().split())
    print(dp[west][east])