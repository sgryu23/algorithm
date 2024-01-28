import sys
from collections import deque
input = sys.stdin.readline


def bfs(subin, sister):
    v = 1  # 가속도
    visited = [[False] * 500001 for _ in range(2)]
    q = deque([subin])

    while q:
        sister += v

        if sister > 500000:
            return -1

        if visited[v % 2][sister]:
            return v

        len_q = len(q)
        for _ in range(len_q):
            x = q.popleft()

            for now in [x - 1, x + 1, 2 * x]:
                if now == sister:
                    return v
                if now < 0 or now > 500000 or visited[v % 2][now]:
                    continue
                visited[v % 2][now] = True
                q.append(now)
        v += 1

    return -1


n, k = map(int, input().split())   # n: 수빈이의 위치, k: 동생의 위치
if n == k:
    print(0)
else:
    ans = bfs(n, k)
    print(ans)