import sys
input = sys.stdin.readline

s1 = [''] + list(input().rstrip())
s2 = [''] + list(input().rstrip())
l1 = len(s1)
l2 = len(s2)
dp = [[''] * l2 for _ in range(l1)]

for i in range(1, l1):
    for j in range(1, l2):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i-1][j-1] + s1[i]
        else:
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

ans = dp[-1][-1]
if len(ans) == 0:
    print(len(ans))
else:
    print(len(ans))
    print(ans)