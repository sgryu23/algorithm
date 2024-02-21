import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input())
room = []
visited = [[n ** 2 for c in range(n)] for r in range(n)]
visited[0][0] = 0
heap = [[0, 0, 0]]
for _ in range(n):
    room.append(list(map(int, input().rstrip())))

while heap:
    val, row, col = heappop(heap)

    if visited[row][col] < val:
        continue

    for nr, nc in [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]:
        if 0 <= nr < n and 0 <= nc < n:
            new_val = val
            # 검은 방인 경우
            if room[nr][nc] == 0:
                new_val = val + 1
            if visited[nr][nc] > new_val:
                visited[nr][nc] = new_val
                heappush(heap, [new_val, nr, nc])

print(visited[-1][-1])