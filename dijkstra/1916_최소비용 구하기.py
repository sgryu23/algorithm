import sys
import heapq
input = sys.stdin.readline


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        cost, now = heapq.heappop(q)
        if distance[now] < cost:
            continue

        for i in arr[now]:
            spend = cost + i[1]
            if spend < distance[i[0]]:
                distance[i[0]] = spend
                heapq.heappush(q, (spend, i[0]))


N = int(input())  # N: 도시의 개수
M = int(input())  # M: 버스의 개수
arr = [[] * N for _ in range(N+1)]
for _ in range(M):
    s, e, c = map(int, input().split())
    arr[s].append((e, c))
st, destination = map(int, input().split())

INF = float('inf')
distance = [INF] * (N+1)

dijkstra(st)
# print(distance)
print(distance[destination])
