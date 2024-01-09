import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]
shark = 2  # 아기 상어의 크기
had = 0   # 아기 상어가 먹은 물고기
time = 0   # 걸린 시간(답으로 출력할 것)
time_add = 0

# 아기 상어의 위치를 찾기 & 해당 좌표 저장 후 0으로 바꾸기
findShark = False
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            shark_r, shark_c = i, j
            arr[i][j] = 0

# 먹을 물고기가 있는 동안 반복
while True:
    remaining_pray = False
    for i in range(N):
        for j in range(N):
            if 0 < arr[i][j] < shark:
                remaining_pray = True
    if not remaining_pray:
        break
    pos = deque()
    pos.append((shark_r, shark_c, 0))
    visited = [[False] * N for _ in range(N)]
    visited[shark_r][shark_c] = True
    cand = []
    while not cand and pos:
        time_add += 1
        for p in range(len(pos)):
            r, c, distance = pos.popleft()
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < N and 0 <= nc < N:
                    # 이동할 수 있으면 pos에 append
                    if 0 < arr[nr][nc] < shark:  # 먹을 수 있다면
                        cand.append((nr, nc, distance + 1))
                        visited[nr][nc] = True
                    elif arr[nr][nc] == 0 or arr[nr][nc] == shark:
                        if not visited[nr][nc]:
                            pos.append((nr, nc, distance + 1))
                            visited[nr][nc] = True
    if not pos and not cand:  # 먹이는 있는데 아기 상어가 움직이지 못하는 경우 탈출 조건(시간 초과 원인 1)
        # time -= 1
        break
    if cand:
        cand = sorted(cand, key=lambda x: (x[2], x[0], x[1]))
        had += 1
        if had == shark:
            shark += 1
            had = 0
        shark_r, shark_c = cand[0][0], cand[0][1]
        arr[shark_r][shark_c] = 0
        time += time_add
        time_add = 0

print(time)