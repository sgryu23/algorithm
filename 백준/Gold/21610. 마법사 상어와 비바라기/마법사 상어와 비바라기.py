from collections import deque
# 1. 입력값 받기
N, M = map(int, input().split())  # N: 한 변의 길이, M: 이동 횟수
grid = [list(map(int, input().split())) for _ in range(N)]

# 비바라기 시전 시에 생기는 비구름 좌표
cloud = deque()
cloud.append((N-2, 0))
cloud.append((N-2, 1))
cloud.append((N-1, 0))
cloud.append((N-1, 1))
delta = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))

for _ in range(M):
    d, s = map(int, input().split())  # d: 방향, s: 거리
    for_duplicate = []
    move_i, move_j = delta[d-1]
    for cl in cloud:
        cloud_i, cloud_j = cl
        ni = cloud_i + move_i * s
        nj = cloud_j + move_j * s

        # 구름 이동 후 비가 1씩 내림
        while ni < 0 or ni >= N:
            if ni < 0:
                ni += N
            elif ni >= N:
                ni -= N
        while nj < 0 or nj >= N:
            if nj < 0:
                nj += N
            elif nj >= N:
                nj -= N
        grid[ni][nj] += 1
        for_duplicate.append((ni, nj))

    # 비 내리고 구름 없애기
    cloud.clear()

    # 물 복사 버그 시전
    for duplicate in for_duplicate:
        dup_r, dup_c = duplicate
        for i in range(4):
            tmp_r, tmp_c = delta[2 * i + 1]
            is_water_row = dup_r + tmp_r
            is_water_col = dup_c + tmp_c
            if 0 <= is_water_row < N and 0 <= is_water_col < N:
                if grid[is_water_row][is_water_col]:
                    grid[dup_r][dup_c] += 1

    # 구름이 있었던 칸을 제외 & 물의 양이 2 이상인 칸에 구름이 생김 & 물의 양이 2만큼 줄어듦
    for i in range(N):
        for j in range(N):
            if grid[i][j] >= 2 and (i, j) not in for_duplicate:
                cloud.append((i, j))
                grid[i][j] -= 2

ans = 0
for r in range(N):
    ans += sum(grid[r])
print(ans)