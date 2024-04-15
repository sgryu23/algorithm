import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
maze = []
escape = False
answer = 0

for r in range(R):
    maze.append(list(input().rstrip()))

visited = [[0 for c in range(C)] for r in range(R)]

fire = deque()
Jihoon = deque()

for row in range(R):
    for col in range(C):
        if maze[row][col] == 'J':
            Jihoon.append((row, col))
            visited[row][col] = 1
        elif maze[row][col] == 'F':
            fire.append((row, col))
            visited[row][col] = 1

while Jihoon and not escape:
    answer += 1
    for _ in range(len(Jihoon)):
        j_row, j_col = Jihoon.popleft()


        for new_row, new_col in [[j_row + 1, j_col], [j_row, j_col + 1], [j_row - 1, j_col], [j_row, j_col - 1]]:
            if 0 <= new_row < R and 0 <= new_col < C:
                if maze[new_row][new_col] == '.' and visited[new_row][new_col] == 0:
                    Jihoon.append((new_row, new_col))
                    maze[new_row][new_col] = 'J'
                    visited[new_row][new_col] = 1
            else:
                escape = True

    for _ in range(len(fire)):
        f_row, f_col = fire.popleft()

        for new_row, new_col in [[f_row + 1, f_col], [f_row, f_col + 1], [f_row - 1, f_col], [f_row, f_col - 1]]:
            if 0 <= new_row < R and 0 <= new_col < C:
                if maze[new_row][new_col] == '.' or maze[new_row][new_col] == 'J':
                    fire.append((new_row, new_col))
                    maze[new_row][new_col] = 'F'
                    if (new_row, new_col) in Jihoon:
                        Jihoon.remove((new_row, new_col))

if escape:
    print(answer)
else:
    print('IMPOSSIBLE')