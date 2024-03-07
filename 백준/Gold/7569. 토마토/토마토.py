from collections import deque

# 1. 입력 값 받기
cols, rows, height = map(int, input().split())
# boxes[h][r][c] 로 표현됨
boxes = list([list(map(int, input().split())) for _ in range(rows)] for h in range(height))
visited = boxes.copy()

# 2. 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 방향에 대한 델타 구현
dr = [0, 0, 0, 0, 1, -1]
dc = [0, 0, -1, 1, 0, 0]
dh = [1, -1, 0, 0, 0, 0]

# 3. 최소 일수 => BFS로 구현(0 인 지역만 큐에 담도록)
dq = deque()
for h in range(height):
    for r in range(rows):
        for c in range(cols):
            if boxes[h][r][c] == 1:
                dq.append((h, r, c))
                visited[h][r][c] = 1

day = 0

while dq:
    for length in range(len(dq)):
        hh, rr, cc = dq.popleft()
        for k in range(6):
            nh = hh + dh[k]
            nr = rr + dr[k]
            nc = cc + dc[k]
            if 0 <= nh < height and 0 <= nr < rows and 0 <= nc < cols and visited[nh][nr][nc] != 1 and boxes[nh][nr][nc] == 0:
                dq.append((nh, nr, nc))
                visited[nh][nr][nc] = 1
    day += 1

# 4. 갈 수 있는 곳을 다 돌았을 때
for th in range(height):
    for tr in range(rows):
        for tc in range(cols):
            if boxes[th][tr][tc] == 0:
                print(-1)
                quit()

# 5. 최종 답 출력
if day > 0:
    print(day - 1)
else:
    print(day)