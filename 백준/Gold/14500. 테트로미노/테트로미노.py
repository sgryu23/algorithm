# 가지치기를 잘 해야겠는데

import sys
input = sys.stdin.readline


def tetromino(num, val, i, j):
    global max_val
    if num == 1:
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < rows and 0 <= nj < cols and not visited[ni][nj]:
                if val + arr[ni][nj] > max_val:
                    max_val = val + arr[ni][nj]
        return
    for k in range(4):
        nr = i + di[k]
        nc = j + dj[k]
        if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
            visited[nr][nc] = 1
            tetromino(num-1, val+arr[nr][nc], nr, nc)
            visited[nr][nc] = 0


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
max_val = 0

rows, cols = map(int, input().split())
arr = []
for _ in range(rows):
    arr.append(list(map(int, input().split())))

visited = [[0] * cols for _ in range(rows)]

for r in range(rows):
    for c in range(cols):
        visited[r][c] = 1
        tetromino(3, arr[r][c], r, c)
        # ㅜ 모양 탐색
        tmp = []
        for l in range(4):
            rr = r + di[l]
            cc = c + dj[l]
            if 0 <= rr < rows and 0 <= cc < cols:
                tmp.append(arr[rr][cc])
        if len(tmp) >= 3:
            if len(tmp) == 3:
                if sum(tmp) + arr[r][c] > max_val:
                    max_val = sum(tmp) + arr[r][c]
            elif len(tmp) == 4:
                min_val = min(tmp)
                if sum(tmp) + arr[r][c] - min_val > max_val:
                    max_val = sum(tmp) + arr[r][c] - min_val
        else:
            pass
        visited[r][c] = 0

print(max_val)