import sys
from collections import deque
input = sys.stdin.readline


def bfs(v):
    global ans
    dq.append(v)
    visited[v] = 1
    color = 2

    while dq:
        now = dq.popleft()
        if visited[now] == 1:
            color = 2
        else:
            color = 1

        for j in arr[now]:
            if visited[j] == 0:
                visited[j] = color
                dq.append(j)
            else:
                if visited[now] == visited[j]:
                    ans = 'impossible'
        if ans == 'impossible':
            break


T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    dq = deque()
    ans = 'possible'
    visited = [0] * (n + 1)
    arr = [[] for _ in range(n + 1)]
    for mm in range(m):
        x, y = map(int, input().split())
        arr[x].append(y)
        arr[y].append(x)

    for i in range(1, n + 1):
        if visited[i] == 0:
            bfs(i)

    print(ans)