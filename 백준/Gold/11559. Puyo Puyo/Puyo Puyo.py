import sys
from collections import deque
input = sys.stdin.readline

field = []
answer = 0

for _ in range(12):
    field.append(list(input().rstrip()))

while True:
    # 1. 연쇄가 가능한지 탐색
    visited = [[0 for c in range(6)] for r in range(12)]
    splash = False

    for row in range(11, -1, -1):
        for col in range(6):
            if field[row][col] != '.' and visited[row][col] == 0:
                dq = deque()
                dq.append((row, col))
                visited[row][col] = 1
                candidate = [(row, col)]
                color = field[row][col]
                same_color_count = 1
                while dq:
                    r, c = dq.popleft()
                    for nr, nc in [[r + 1, c], [r, c + 1], [r - 1, c], [r, c - 1]]:
                        if 0 <= nr < 12 and 0 <= nc < 6:
                            if field[nr][nc] == color and visited[nr][nc] == 0:
                                visited[nr][nc] = 1
                                dq.append((nr, nc))
                                candidate.append((nr, nc))
                                same_color_count += 1

                if same_color_count >= 4:
                    splash = True  # 터졌음을 나타내는 상태 변경
                    for (r, c) in candidate:
                        field[r][c] = '.'

    # 터진 적이 있으면 연쇄 횟수 +1, 없으면 중단
    if splash:
        answer += 1
        # 하나씩 아래로 내려주기
        for col in range(6):
            for row in range(11, -1, -1):
                if field[row][col] != '.' and row < 11:
                    fall_down = 0
                    while row + fall_down < 11 and field[row + fall_down + 1][col] == '.':
                        fall_down += 1
                    if row + fall_down != row:
                        field[row + fall_down][col] = field[row][col]
                        field[row][col] = '.'
    else:
        break

print(answer)