import sys
from collections import deque

input = sys.stdin.readline


# 안전 거리 구하는 함수 만들기
def safe_distance(row, col):
    dq = deque()
    visited = [[0] * M for _ in range(N)]
    distance = 1
    dq.append((row, col))
    visited[row][col] = 1

    while dq:
        for k in range(len(dq)):
            r, c = dq.popleft()
            for d in range(8):
                nr = r + di[d]
                nc = c + dj[d]
                if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] > -1:
                    # 거리가 갱신되지 않은 경우
                    if arr[nr][nc] == 0 and not visited[nr][nc]:
                        arr[nr][nc] = distance
                        dq.append((nr, nc))
                        visited[nr][nc] = 1
                    # 한 번이라도 온 적이 있는 경우
                    elif arr[nr][nc] > 0 and not visited[nr][nc]:
                        if arr[nr][nc] > distance:
                            arr[nr][nc] = distance
                            dq.append((nr, nc))
                            visited[nr][nc] = 1
                        else:
                            visited[nr][nc] = 1

        distance += 1
        # print(arr)


N, M = map(int, input().split())    # N: 행의 수, M: 열의 수
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

di = [0, 1, 0, -1, 1, 1, -1, -1]
dj = [1, 0, -1, 0, 1, -1, 1, -1]

# 아기 상어가 있는 곳은 -1로 놓고 거리를 각 그래프 좌표에 갱신하면서 바꿔줄 생각
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            arr[i][j] = -1

max_distance = 0

for x in range(N):
    for y in range(M):
        if arr[x][y] == -1:
            safe_distance(x, y)

for rr in range(N):
    max_distance = max(max_distance, max(arr[rr]))
print(max_distance)