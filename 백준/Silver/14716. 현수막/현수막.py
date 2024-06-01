import sys
input = sys.stdin.readline

delta = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

M, N = map(int, input().split())
array = []
answer = 0

for _ in range(M):
    array.append(list(map(int, input().split())))

visited = [[0 for c in range(N)] for r in range(M)]

for row in range(M):
    for column in range(N):
        if array[row][column] == 1 and visited[row][column] == 0:
            stack = [(row, column)]
            visited[row][column] = 1
            answer += 1

            while stack:
                r, c = stack.pop()

                for d_row, d_col in delta:
                    n_row, n_col = r + d_row, c + d_col
                    if 0 <= n_row < M and 0 <= n_col < N:
                        if array[n_row][n_col] == 1 and visited[n_row][n_col] == 0:
                            visited[n_row][n_col] = 1
                            stack.append((n_row, n_col))
print(answer)