import sys
input = sys.stdin.readline

N = int(input())
mod = 1000000000

# dp: 길이가 len이고 1의 자리수가 num이며 사용한 숫자가 state인 계단 수의 개수
dp = [[0 for _ in range(1 << 10)] for _ in range(10)]

# 시작자리 1로 설정해준다.
for i in range(1, 10):
    dp[i][1 << i] = 1

# 자릿수만큼 순회
for j in range(1, N):
    # 각 자릿수에서의 정보를 담을 배열
    memo = [[0 for _ in range(1 << 10)] for _ in range(10)]
    for k in range(10):
        for l in range(1024):
            if k < 9:
                memo[k][l | (1 << k)] = (memo[k][l | (1 << k)] + dp[k + 1][l]) % mod
            if k > 0:
                memo[k][l | (1 << k)] = (memo[k][l | (1 << k)] + dp[k - 1][l]) % mod

    dp = memo

print(sum(dp[i][1023] for i in range(10)) % mod)