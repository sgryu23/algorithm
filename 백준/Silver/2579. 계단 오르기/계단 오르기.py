n = int(input())       # 계단 개수
stairs = [int(input()) for _ in range(n)]  # 계단 리스트로 저장
dp = [0] * n           # dp 리스트
if len(stairs) <= 2:   # 계단이 2 개 이하라면 다 더해서 출력
    print(sum(stairs))
else:
    dp[0] = stairs[0]              # 첫 계단의 합
    dp[1] = stairs[1] + stairs[0]  # 둘째 계단까지의 합
    for i in range(2, n):
        dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i -2] + stairs[i])
    print(dp[-1])