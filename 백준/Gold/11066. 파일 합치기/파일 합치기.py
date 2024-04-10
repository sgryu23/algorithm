import sys

T = int(input())  # T: 테스트 케이스
for i in range(T):
    K = int(input())  # K: 소설을 구성하는 장의 수
    files = list(map(int, sys.stdin.readline().split()))
    # 1. 누적합을 구한다.
    accumulative_sum = [0] * (K + 1)
    for j in range(1, K + 1):
        accumulative_sum[j] = accumulative_sum[j - 1] + files[j - 1]

    dp = [[0 for c in range(K + 1)] for r in range(K + 1)]
    for r in range(1, K):
        for c in range(1, K - r + 1):
            # c ~ c + r까지의 부분 합
            dp[c][c + r] = min([dp[c][k] + dp[k + 1][c + r] for k in range(c, c + r)]) + (accumulative_sum[c + r] - accumulative_sum[c - 1])
    
    print(dp[1][K])