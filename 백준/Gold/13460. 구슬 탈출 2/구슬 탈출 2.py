import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def move(x, y, i, j):
    _count = 0
    while board[x + i][y + j] != '#' and board[x][y] != 'O':
        x += i
        y += j
        _count += 1
    return x, y, _count


def bfs():
    while queue:
        rx, ry, bx, by, cnt = queue.popleft()

        if cnt > 10:
            break
        for i in range(4):
            nrx, nry, r_count = move(rx, ry, dx[i], dy[i])
            nbx, nby, b_count = move(bx, by, dx[i], dy[i])

            if board[nbx][nby] == 'O':
                continue

            if board[nrx][nry] == 'O':
                return cnt

            if nrx == nbx and nry == nby:
                if r_count > b_count:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if [nrx, nry, nbx, nby] not in visited:
                visited.append([nrx, nry, nbx, nby])
                queue.append([nrx, nry, nbx, nby, cnt + 1])

    return -1


N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
visited = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
queue = deque()

rx = ry = bx = by = 0

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
        if board[i][j] == 'B':
            bx, by = i, j

queue.append([rx, ry, bx, by, 1])
visited.append([rx, ry, bx, by])

print(bfs())