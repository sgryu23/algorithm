import sys
input = sys.stdin.readline


def rental_cost(r, c, flowers):
    global minimum_cost, cost
    # 종료 조건
    if flowers == 3:
        minimum_cost = min(minimum_cost, cost)
        return

    for _r in range(1, N - 1):
        for _c in range(1, N - 1):
            if visited[_r][_c] == visited[_r - 1][_c] == visited[_r + 1][_c] == visited[_r][_c + 1] == visited[_r][_c - 1] ==0:
                if abs(_r - r) + abs(_c - c) > 2:
                    visited[_r][_c] = visited[_r - 1][_c] = visited[_r + 1][_c] = visited[_r][_c - 1] = visited[_r][_c + 1] = 1
                    cost += cost_for_rent[_r][_c]
                    rental_cost(_r, _c, flowers + 1)
                    cost -= cost_for_rent[_r][_c]
                    visited[_r][_c] = visited[_r - 1][_c] = visited[_r + 1][_c] = visited[_r][_c - 1] = visited[_r][_c + 1] = 0


N = int(input())  # N: 화단의 한 변의 길이
grid = []

for _ in range(N):
    grid.append(list(map(int, input().split())))

minimum_cost = sys.maxsize  # minimum_cost: 구하고자 하는 답

# 1. 꽃이 피었을 때 각 땅을 빌렸을 때의 비용
cost_for_rent = [[0 for c in range(N)] for r in range(N)]

for i in range(1, N - 1):
    for j in range(1, N - 1):
        for nr, nc in [[i, j], [i, j + 1], [i + 1, j], [i, j - 1], [i - 1, j]]:
            cost_for_rent[i][j] += grid[nr][nc]

# 2. 꽃을 하나씩 심을 떄 드는 비용 최솟값을 완전 탐색으로 구하기
for row in range(1, N - 1):
    for column in range(1, N - 1):
        visited = [[0 for c in range(N)] for r in range(N)]
        cost = 0
        visited[row][column] = visited[row - 1][column] = visited[row + 1][column] = visited[row][column - 1] = visited[row][column + 1] = 1
        cost += cost_for_rent[row][column]
        rental_cost(row, column, 1)

print(minimum_cost)