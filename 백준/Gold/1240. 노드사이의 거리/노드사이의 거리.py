import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())  # N: 노드의 개수, M: 노드 쌍의 개수

tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    dot_1, dot_2, distance = map(int, input().split())
    tree[dot_1].append([dot_2, distance])
    tree[dot_2].append([dot_1, distance])

for _ in range(M):
    start, end = map(int, input().split())
    visited = [0 for _ in range(N + 1)]
    visited[start] = 1
    dq = deque()
    dq.append((start, 0))
    find_answer = False

    while dq and not find_answer:
        now, dis = dq.popleft()
        for adj_node, _distance in tree[now]:
            if visited[adj_node] == 0:
                _distance += dis
                visited[adj_node] = 1
                if adj_node == end:
                    print(_distance)
                    find_answer = True
                    break

                dq.append((adj_node, _distance))