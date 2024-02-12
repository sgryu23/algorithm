import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline


def is_early_adaptor(current_node):
    visited[current_node] = 1
    for adj_node in friends[current_node]:
        if not visited[adj_node]:
            is_early_adaptor(adj_node)
            # 자신이 얼리 어답터가 아니면 자식 노드가 얼리 어답터
            dp[current_node][0] += dp[adj_node][1]
            # 자신이 얼리 어답터면 자식 노드는 상관 X
            dp[current_node][1] += min(dp[adj_node])


n = int(input())  # n: 트리의 정점 개수
friends = [[] for _ in range(n + 1)]
for relation in range(1, n):
    u, v = map(int, input().split())
    friends[u].append(v)
    friends[v].append(u)

visited = [0] * (n + 1)
dp = [[0, 1] for _ in range(n + 1)]

is_early_adaptor(1)

print(min(dp[1]))