import sys
from collections import deque
input = sys.stdin.readline

k = int(input())  # k: 테스트 케이스의 개수
for testcase in range(k):
    v, e = map(int, input().split())  # v: 정점 개수, e: 간선 개수
    graph = [[] for _ in range(v + 1)]
    for adj_node in range(e):
        a, b = map(int, input().split())  # a, b: 인접한 정점의 번호
        graph[a].append(b)
        graph[b].append(a)
    visited = [0] * (v + 1)
    is_connected = [0] * (v + 1)
    answer = True
    for i in range(1, v + 1):
        if graph[i] and not visited[i] and answer:
            connected = 1
            dq = deque()
            dq.append(i)
            if not is_connected[i]:
                is_connected[i] = connected
            while dq and answer:
                now = dq.popleft()
                if visited[now]:
                    continue
                visited[now] = True
                if is_connected[now] == 1:
                    connected = 2
                else:
                    connected = 1

                for j in graph[now]:
                    if is_connected[j] != 0 and is_connected[j] == is_connected[now]:
                        answer = False
                        break
                    is_connected[j] = connected
                    dq.append(j)
    if answer:
        print('YES')
    else:
        print('NO')