import sys
from collections import deque
input = sys.stdin.readline

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N = int(input())
arr = [[0] * (N + 1) for _ in range(N + 1)]
K = int(input())
for k in range(K):
    r, c = map(int, input().split())
    arr[r][c] = 9
L = int(input())
dq = deque()
now, now_dir, now_row, now_col = 0, 0, 1, 1
snake = 1
arr[now_row][now_col] = 1
dq.append((now_row, now_col))

for l in range(L):
    X, C = input().split()
    X = int(X)
    while now < X:
        now += 1
        # 벽에 부딪히지 않는 경우
        if 1 <= now_row + di[now_dir] <= N and 1 <= now_col + dj[now_dir] <= N:
            # 이동한 칸에 사과가 있는 경우
            if arr[now_row + di[now_dir]][now_col + dj[now_dir]] == 9:
                arr[now_row + di[now_dir]][now_col + dj[now_dir]] = 1
                dq.append((now_row + di[now_dir], now_col + dj[now_dir]))
                now_row += di[now_dir]
                now_col += dj[now_dir]
                snake += 1
            # 이동한 칸에 사과가 없는 경우
            elif arr[now_row + di[now_dir]][now_col + dj[now_dir]] == 0:
                arr[now_row + di[now_dir]][now_col + dj[now_dir]] = 1
                dq.append((now_row + di[now_dir], now_col + dj[now_dir]))
                now_row += di[now_dir]
                now_col += dj[now_dir]
            # 자기 몸인 경우
            elif arr[now_row + di[now_dir]][now_col + dj[now_dir]] == 1:
                print(now)
                quit()
            while len(dq) > snake:
                delete_row, delete_col = dq.popleft()
                arr[delete_row][delete_col] = 0
        # 벽에 부딪히는 경우(종료)
        else:
            print(now)
            quit()
    if C == 'D':
        now_dir = (now_dir + 1) % 4
    else:
        now_dir = (now_dir - 1) % 4

while True:
    now += 1
    # 벽에 부딪히지 않는 경우
    if 1 <= now_row + di[now_dir] <= N and 1 <= now_col + dj[now_dir] <= N:
        # 이동한 칸에 사과가 있는 경우
        if arr[now_row + di[now_dir]][now_col + dj[now_dir]] == 9:
            arr[now_row + di[now_dir]][now_col + dj[now_dir]] = 1
            dq.append((now_row + di[now_dir], now_col + dj[now_dir]))
            now_row += di[now_dir]
            now_col += dj[now_dir]
            snake += 1
        # 이동한 칸에 사과가 없는 경우
        elif arr[now_row + di[now_dir]][now_col + dj[now_dir]] == 0:
            arr[now_row + di[now_dir]][now_col + dj[now_dir]] = 1
            dq.append((now_row + di[now_dir], now_col + dj[now_dir]))
            now_row += di[now_dir]
            now_col += dj[now_dir]
        # 자기 몸인 경우
        elif arr[now_row + di[now_dir]][now_col + dj[now_dir]] == 1:
            print(now)
            quit()
        while len(dq) > snake:
            delete_row, delete_col = dq.popleft()
            arr[delete_row][delete_col] = 0
    # 벽에 부딪히는 경우(종료)
    else:
        print(now)
        quit()