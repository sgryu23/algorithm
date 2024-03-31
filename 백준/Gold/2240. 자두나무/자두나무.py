import sys
input = sys.stdin.readline

T, W = map(int, input().split())  # T: 자두가 떨어지는 횟수, W: 움직이는 횟수
plum_tree = [0]
for _ in range(T):
    plum_tree.append(int(input()))

dp = [[0 for c in range(W + 1)] for r in range(T + 1)]

for i in range(1, T + 1):
    if plum_tree[i] == 1:
        dp[i][0] = dp[i - 1][0] + 1
    else:
        dp[i][0] = dp[i - 1][0]
    for j in range(1, W + 1):
        # 1번 위치로 떨어지고, 짝수 번 움직이면 -> 1번에서 시작이니까 짝수번 움직이면 1번에 있다.
        if plum_tree[i] == 1 and j % 2 == 0:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + 1
        # 자두 위치 2번, 홀수 번 움직였으면 같은 논리로 자두를 먹을 수 있음
        elif plum_tree[i] == 2 and j % 2 == 1:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + 1
        # 현재 위치에서 자두를 못 먹는 경우
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j])

print(max(dp[T]))