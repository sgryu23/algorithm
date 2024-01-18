import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())  # N: 사다리의 수, M: 뱀의 수
board = [0] * 101
visited = [0] * 101
for n in range(N + M):
    x, y = map(int, input().split())  # x 번 칸에 도착하면 y번 칸으로 이동
    board[x] = y

dq = deque()
dq.append([1, 0])
visited[1] = 1

while True:
    now, cnt = dq.popleft()
    if now == 100:
        print(cnt)
        break

    for i in range(1, 7):
        if now + i <= 100 and not visited[now + i]:
            visited[now + i] = 1
            if board[now + i] == 0:
                dq.append((now + i, cnt + 1))
            else:
                dq.append((board[now + i], cnt + 1))