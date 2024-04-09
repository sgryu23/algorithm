import sys
input = sys.stdin.readline

n = int(input())  # n: 행렬의 크기
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(2)]

P = int(input())  # P: 중간에 거쳐야 하는 원소의 개수
for i in range(P):
    ri, ci = map(int, input().split())
    dp[1][ri - 1][ci - 1] = -1

for row in range(n):
    for col in range(n):
        if row == 0:
            dp[0][row][col] = dp[0][row][col - 1] + arr[row][col]
        elif col == 0:
            dp[0][row][col] = dp[0][row - 1][col] + arr[row][col]
        else:
            dp[0][row][col] = max(dp[0][row - 1][col], dp[0][row][col - 1]) + arr[row][col]

for row in range(n):
    for col in range(n):
        if dp[1][row][col] == -1:
            dp[1][row][col] = max(dp[1][row - 1][col], dp[1][row][col - 1], dp[0][row][col])
        elif dp[1][row][col] == 0:
            if dp[1][row - 1][col] == 0 and dp[1][row][col - 1] == 0:
                dp[1][row][col] = 0
            else:
                dp[1][row][col] = max(dp[1][row - 1][col], dp[1][row][col - 1]) + arr[row][col]

print(dp[1][n - 1][n - 1])