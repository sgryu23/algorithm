import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)
dp[0] = 1
if N > 1:  # 이 경우를 고려 안 해서 걸림
    dp[2] = 3  # N == 2 => 3 가지 경우
    for i in range(4, N + 1, 2):
        dp[i] = dp[i - 2] * 4 - dp[i -  4]
print(dp[N])


# 테스트 케이스
# N : 1 ANS : 0
# N : 2 ANS : 3
# N : 3 ANS : 0
# N : 4 ANS : 11
# N : 5 ANS : 0
# N : 6 ANS : 41
# N : 7 ANS : 0
# N : 8 ANS : 153
# N : 9 ANS : 0
# N : 10 ANS : 571
# N : 30 ANS : 299303201