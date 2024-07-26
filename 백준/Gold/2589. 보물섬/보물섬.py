import sys
from collections import deque
input = sys.stdin.readline

h, w = map(int, input().split())
arr = []
answer = 0

for _ in range(h):
    arr.append(list(input().rstrip()))

for r in range(h):
    for c in range(w):
        if arr[r][c] == 'L':
            visited = [[-1 for col in range(w)] for row in range(h)]
            visited[r][c] = 0
            dq = deque()
            dq.append((r, c))

            while dq:
                row, col = dq.popleft()

                for nr, nc in [[row + 1, col], [row, col + 1], [row - 1, col], [row, col - 1]]:
                    if 0 <= nr < h and 0 <= nc < w and arr[nr][nc] == 'L' and visited[nr][nc] == -1:
                        visited[nr][nc] = visited[row][col] + 1
                        if visited[nr][nc] > answer:
                            answer = visited[nr][nc]
                        dq.append((nr, nc))

print(answer)