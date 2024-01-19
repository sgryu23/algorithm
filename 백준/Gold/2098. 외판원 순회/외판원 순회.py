import sys
input = sys.stdin.readline


def dfs(current, visited):
    # 1. 이미 방문했으면 저장된 값을 반환
    if dp[current][visited] != INF:
        return dp[current][visited]

    # 2. 만약 모든 노드를 모두 방문했으면 중단
    if visited == ((1 << (N - 1)) - 1):
        if arr[current][start_node]:  # dp[current][visited] = arr[current][start_node]이다.
            dp[current][visited] = arr[current][start_node]
        else:   # arr[current][start_node]에 길이 없다면 INF + 1로 업데이트 해준다 (방문했다는 것을 표시)
            dp[current][visited] = INF + 1
        return dp[current][visited]

    for i in range(1, N):
        if arr[current][i] == 0:  # 현재 노드에서 다음 노드까지 길이 없다면 무시
            continue
        if visited & (1 << (i - 1)):  # 다음 노드가 방문한 노드라면 무시
            continue

        # 방문하지 않은 노드에 대해서 현재 노드에서 그 노드로 가는 길이 있다면 dp 값을 업데이트
        dp[current][visited] = min(dp[current][visited], arr[current][i] + dfs(i, visited | 1 << (i - 1)))

    if dp[current][visited] == INF:
        # 어떤 노드가 다음 노드로 가는 길이 없어서 update가 하나도 되지 않았다면 방문했다는 의미로 INF + 1
        dp[current][visited] = INF + 1

    return dp[current][visited]


N = int(input())  # N: 도시의 수
arr = []
for j in range(N):
    arr.append(list(map(int, input().split())))
INF = 16000000  # 각 행렬의 성분은 1,000,000 이하 & 도시의 수는 16 이하
start_node = 0
dp = [[INF for _ in range(1 << (N - 1))] for _ in range(N)]

print(dfs(0, 0))