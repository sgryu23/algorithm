import sys
input = sys.stdin.readline

# 아이디어 정리
# 연결 요소의 개수를 찾는 것
# 단, 사이클이 있으면 연결 요소 카운팅 하지 않음


def is_cycle(v):
    # 간선 위치에서 시작해서 사이클이 있는지 판단하는 함수
    for adj_node in graph[v]:
        # 인접 노드가 부모 노드면 패스
        if parent[v] == adj_node:
            continue

        # 인접 노드가 부모 노드가 아닌데 방문 했다: 사이클이다
        if visited[adj_node]:
            return True

        parent[adj_node] = v
        visited[adj_node] = 1
        # 인접 노드를 루트 노드로 하는 서브 트리에 사이클이 존재해도
        # 사이클이 있는 트리이므로 사이클 True 반환
        if is_cycle(adj_node):
            return True

    return False


test_case = 0

while True:
    n, m = map(int, input().split())  # n: 정점의 개수, m: 간선의 개수
    if n == m == 0:
        break
    test_case += 1
    trees = 0
    parent = [-1] * (n + 1)
    visited = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for node in range(1, n + 1):
        if visited[node] == 0:
            parent[node] = node
            visited[node] = 1
            if not is_cycle(node):
                trees += 1

    if trees == 0:
        print(f'Case {test_case}: No trees.')
    elif trees == 1:
        print(f'Case {test_case}: There is one tree.')
    else:
        print(f'Case {test_case}: A forest of {trees} trees.')