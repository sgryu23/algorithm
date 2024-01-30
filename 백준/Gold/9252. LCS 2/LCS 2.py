import sys
input = sys.stdin.readline

string1 = [''] + list(input().rstrip())
string2 = [''] + list(input().rstrip())
len_str1 = len(string1) - 1
len_str2 = len(string2) - 1

dp = [['' for i in range(len_str1 + 1)] for _ in range(len_str2 + 1)]
for row in range(1, len_str2 + 1):
    for col in range(1, len_str1 + 1):
        # 두 문자열이 일치하는 경우
        if string2[row] == string1[col]:
            dp[row][col] = dp[row - 1][col - 1] + string1[col]
        # 일치하지 않는 경우
        else:
            if len(dp[row - 1][col]) >= len(dp[row][col - 1]):
                dp[row][col] = dp[row - 1][col]
            else:
                dp[row][col] = dp[row][col - 1]

ans = dp[-1][-1]
print(len(ans))
if len(ans) > 0:
    print(ans)