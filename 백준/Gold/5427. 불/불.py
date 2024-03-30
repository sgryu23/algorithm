import sys
from collections import deque
input = sys.stdin.readline

test_case = int(input())
for tc in range(test_case):
    w, h = map(int, input().split())  # w: 너비, h: 높이
    arr = []
    for _ in range(h):
        arr.append(list(input()))

    answer, start_row, start_col = 0, 0, 0
    is_escaped = False

    fire = deque()
    for row in range(h):
        for col in range(w):
            if arr[row][col] == '*':
                fire.append((row, col))
            elif arr[row][col] == '@':
                start_row, start_col = row, col

    me = deque()
    me.append((start_row, start_col))

    while me and not is_escaped:
        answer += 1
        for fire_extension in range(len(fire)):
            fire_row, fire_col = fire.popleft()
            for nr, nc in [[fire_row + 1, fire_col], [fire_row, fire_col + 1], [fire_row - 1, fire_col], [fire_row, fire_col - 1]]:
                if 0 <= nr < h and 0 <= nc < w:
                    if arr[nr][nc] == '.' or arr[nr][nc] == '@':
                        arr[nr][nc] = '*'
                        fire.append((nr, nc))

        for to_go in range(len(me)):
            me_row, me_col = me.popleft()
            for nr, nc in [[me_row + 1, me_col], [me_row, me_col + 1], [me_row - 1, me_col], [me_row, me_col - 1]]:
                if 0 <= nr < h and 0 <= nc < w:
                    if arr[nr][nc] == '.':
                        arr[nr][nc] = '@'
                        me.append((nr, nc))
                else:
                    is_escaped = True

    if not is_escaped:
        print('IMPOSSIBLE')
    else:
        print(answer)