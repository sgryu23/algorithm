import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(start):
    global order
    for adj_node in tree[start]:
        if visited[adj_node] == 0:
            visited[adj_node] = order
            order += 1
            dfs(adj_node)


N, M, R = map(int, input().split())  # N: 정점의 수, M: 간선의 수, R: 시작 정점
tree = [[] for _ in range(N + 1)]
for node in range(M):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

for i in range(N + 1):
    tree[i].sort(reverse=True)

visited = [0 for _ in range(N + 1)]

visited[R] = 1
order = 2

dfs(R)

for answer in visited[1:]:
    print(answer)