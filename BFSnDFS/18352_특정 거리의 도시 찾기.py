import sys
from collections import deque
input = sys.stdin.readline

# N: 도시의 개수, M: 도로의 개수, K: 거리 정보, X: 출발 도시 번호
N, M, K, X = map(int, input().split())
cities = [[] * N for _ in range(N+1)]
for m in range(M):
    A, B = map(int, input().split())
    cities[A].append(B)

visited = [-1] * (N + 1)
ans_list = []
dq = deque()
cnt = 0
dq.append(X)
visited[X] = 0

while dq:
    now = dq.popleft()
    for r in range(len(cities[now])):
        if visited[cities[now][r]] == -1:
            dq.append(cities[now][r])
            visited[cities[now][r]] = visited[now] + 1

if K not in visited:
    print(-1)
else:
    for i in range(1, N+1):
        if visited[i] == K:
            print(i)