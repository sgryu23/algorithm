import sys
input = sys.stdin.readline

n, m = map(int, input().split())                               # n: 활성화 된 앱의 개수, m: 추가로 확보해야 하는 바이트 수
active_memory = [0] + list(map(int, input().split()))          # active_memory: 현재 활성화 중인 앱의 메모리
cost = [0] + list(map(int, input().split()))                   # cost: 앱을 비활성화 했을 때의 비용
sum_cost = sum(cost)

dp = [[0 for _ in range(sum_cost + 1)] for _ in range(n + 1)]  # dp: 메모리를 저장할 dp
min_cost = 10000001

# 추가로 확보해야 하는 바이트의 수가 0인 경우
if m != 0:
    for i in range(1, n + 1):
        memory = active_memory[i]
        c = cost[i]

        for j in range(sum_cost + 1):
            # 현재 앱을 비활성화 할만큼의 cost 가 충족되지 않았을 때(i - 1 행 저장된 값 복사)
            if j < c:
                dp[i][j] = dp[i - 1][j]
            # 현재 앱을 껐을 때 vs 현재 앱을 끄지 않았을 때의 메모리를 비교해서 큰 값을 저장
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - c] + memory)
            # 추가로 필요한 메모리가 확보된 경우
            if dp[i][j] >= m:
                min_cost = min(min_cost, j)

    # sum_cost 가 0 인 반례를 고려
    if sum_cost != 0:
        print(min_cost)
    else:
        print(0)
else:
    print(0)