import sys
input = sys.stdin.readline

# gear 1: idx 2(gear 2)
# gear 2: idx 6(gear 1), idx 2(gear 3)
# gear 3: idx 2(gear 2), idx 6(gear 4)
# gear 4: idx 6(gear 3)
# idx 2, 6의 규칙을 봐야 함
gears = [[0]]

for _ in range(4):
    gears.append(list(map(int, input().rstrip())))

K = int(input())
for _ in range(K):
    gear_num, direction = map(int, input().split())  # direction: 1이면 시계 방향, -1이면 반시계 방향
    rotate = [0 for _ in range(5)]
    rotate[gear_num] = direction
    # 기어 기준으로 오른쪽, 왼쪽
    for num in range(gear_num, 4):   # 오른쪽
        if gears[num][2] != gears[num + 1][6]:
            if rotate[num] == 1:  # 시계 방향으로 돌아가면
                rotate[num + 1] = -1  # 반시계 방향으로 돌아감
            elif rotate[num] == -1:
                rotate[num + 1] = 1  # 시계 방향으로 돌아감
    for num in range(gear_num, 1, -1):  # 왼쪽
        if gears[num][6] != gears[num - 1][2]:
            if rotate[num] == 1:
                rotate[num - 1] = -1
            elif rotate[num] == -1:
                rotate[num - 1] = 1
    # 톱니바퀴 회전
    for r in range(1, 5):
        if rotate[r] == 1:  # 시계 방향으로 회전
            gears[r] = ([gears[r][7]] + gears[r])[:8]
        elif rotate[r] == -1:
            gears[r] = (gears[r] + [gears[r][0]])[1:]

ans = 0
for i in range(1, 5):
    ans += gears[i][0] * (2 ** (i - 1))
print(ans)