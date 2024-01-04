import sys
input = sys.stdin.readline


# Kruskal Algorithm
# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


V, E = map(int, input().split())
parent = [0] * (V + 1)  # 노드의 개수와 간선(union 연산)의 개수 입력 받기
edges = []
result = 0

for i in range(1, V + 1):
    parent[i] = i  # 부모 테이블에서 부모를 자기 자신으로 초기화

# 모든 간선에 대한 정보를 입력받기
for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)