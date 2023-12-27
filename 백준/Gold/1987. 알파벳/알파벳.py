import sys
input = sys.stdin.readline


def dfs(r, c):
    global board, R, C
    max_val = 0
    q = set()  # 세트로 선언
    q.add((r, c, board[r][c]))

    while q:
        row, col, visited = q.pop()
        max_val = max(max_val, len(visited))

        if max_val == 26:
            return 26

        for k in range(4):
            nr = row + dr[k]
            nc = col + dc[k]
            if 0 <= nr < R and 0 <= nc < C and board[nr][nc] not in visited:
                q.add((nr, nc, visited + board[nr][nc]))
    return max_val


R, C = map(int, input().split())  # R: 가로, C: 세로
board = []
for _ in range(R):
    board.append(list(input()))

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

print(dfs(0, 0))