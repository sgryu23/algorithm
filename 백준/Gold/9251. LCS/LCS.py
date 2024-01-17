import sys
input = sys.stdin.readline

string1 = list(input().strip())
string2 = list(input().strip())

dp = [[0] * (len(string1) + 1) for _ in range(len(string2) + 1)]

for row in range(1, len(string2) + 1):
    for col in range(1, len(string1) + 1):
        if string1[col - 1] == string2[row - 1]:
            dp[row][col] = dp[row - 1][col - 1] + 1
        else:
            dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])
print(dp[-1][-1])