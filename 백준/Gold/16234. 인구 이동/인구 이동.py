import sys
sys.setrecursionlimit(10 ** 5)
from collections import deque
input = sys.stdin.readline


def moving(arr, num):
    new_grid = [[0 for col in range(n)] for row in range(n)]
    visited = [[0 for col in range(n)] for row in range(n)]
    check = 1
    flag = False

    for row in range(n):
        for col in range(n):
            if not visited[row][col]:
                dq = deque()
                dq.append((row, col))
                visited[row][col] = check
                population_stack = [arr[row][col]]
                point_stack = [(row, col)]

                while dq:
                    rr, cc = dq.popleft()
                    for nr, nc in [[rr - 1, cc], [rr, cc + 1], [rr + 1, cc], [rr, cc - 1]]:
                        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                            # 국경선을 열 수 있는 경우
                            if l <= abs(arr[rr][cc] - arr[nr][nc]) <= r:
                                flag = True
                                population_stack.append(arr[nr][nc])
                                point_stack.append((nr, nc))
                                visited[nr][nc] = check
                                dq.append((nr, nc))
                            # 국경선을 열 수 없는 경우
                            else:
                                new_grid[nr][nc] = arr[nr][nc]
                check += 1
                new_population = sum(population_stack) // len(population_stack)

                while point_stack:
                    row, col = point_stack.pop()
                    new_grid[row][col] = new_population

    # 만약 전체 배열을 탐색했는데 l 명 이상 r 명 이하인 구역이 없다면 탐색 종료
    if not flag:
        print(num)
    # l 명 이상 r 명 이하인 구역이 있다면 추가로 탐색(dfs)
    else:
        moving(new_grid, num + 1)


n, l, r = map(int, input().split())  # n: 땅의 크기, l: l명 이상, r: r명 이하
grid = []   # grid: 땅 크기
for _ in range(n):
    grid.append(list(map(int, input().split())))

answer = 0

moving(grid, answer)