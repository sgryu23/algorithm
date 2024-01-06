import sys
input = sys.stdin.readline

# 아이디어 정리
# 3차원 배열로 LCS 구현하기

s1 = [''] + list(input().rstrip())
s2 = [''] + list(input().rstrip())
s3 = [''] + list(input().rstrip())
l1 = len(s1)
l2 = len(s2)
l3 = len(s3)

dp = [[[0] * l3 for ll in range(l2)] for lll in range(l1)]

for i in range(1, l1):
    for j in range(1, l2):
        for k in range(1, l3):
            if s1[i] == s2[j] == s3[k]:
                dp[i][j][k] += (dp[i-1][j-1][k-1] + 1)
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

print(dp[-1][-1][-1])