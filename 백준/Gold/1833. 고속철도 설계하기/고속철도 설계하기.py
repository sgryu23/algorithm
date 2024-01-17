import sys
input = sys.stdin.readline


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x, y = find(x), find(y)
    parents[max(x, y)] = min(x, y)


N = int(input())
parents = [i for i in range(N + 1)]
edges = []
cost_graph = []
C, M, ans = 0, 0, []
for _ in range(N):
    cost_graph.append(list(map(int, input().split())))


for row in range(N):
    for col in range(row + 1, N):
        cost = cost_graph[row][col]
        if cost < 0:
            C -= cost
            if find(row + 1) != find(col + 1):
                union(row + 1, col + 1)
            else:
                union(0, min(row + 1, col + 1))
        else:
            edges.append([row + 1, col + 1, cost])
edges.sort(key=lambda x:x[2])  # 비용이 낮은 순으로 정렬
for row, col, cost in edges:
    if find(row) != find(col):
        union(row, col)
        C += cost
        M += 1
        ans.append([row, col])

print(C, M)
for x, y in ans:
    print(x, y)