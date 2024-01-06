import copy
from itertools import permutations

# 1. 입력 값 받기
rows, cols, spin = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(rows)]
spin_list = []
for sp in range(spin):
    r, c, s = map(int, input().split())
    spin_list.append((r, c, s))
ans = float('inf')    # 최솟값을 비교해주면서 갱신

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


# 2. 배열 돌리는 연산 정의하기
def func(table, rotate):
    for rot in rotate:
        row, col, distance = rot
    # distance 값이 row - dis, col - dis 부터 시작해서 row - 1, col - 1 까지만 하면 됨
        for i in range(distance):
            now_r = row - 1 - distance + i
            now_c = col - 1 - distance + i
            tmp = table[now_r][now_c]
            for k in range(4):
                while row - 1 - distance + i <= now_r + dr[k] < row + distance - i and col - 1 - distance + i <= now_c + dc[k] < col + distance - i:
                    table[now_r][now_c] = table[now_r + dr[k]][now_c + dc[k]]
                    now_r += dr[k]
                    now_c += dc[k]
            table[row - 1 - distance + i][col - 1 - distance + i + 1] = tmp

    min_val = float('inf')
    for dog in range(rows):
        min_val = min(min_val, sum(table[dog]))

    return min_val


# 3. 연산 수행 순서: 순열로 풀어보자
for s in permutations(spin_list):
    arr_copy = copy.deepcopy(arr)
    ans = min(ans, func(arr_copy, s))

print(ans)