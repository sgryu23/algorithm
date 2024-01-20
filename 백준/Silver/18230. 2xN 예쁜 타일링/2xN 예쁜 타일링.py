import sys
input = sys.stdin.readline

# 아이디어 정리
# (2 x 2 + 2 x 1의 합) & (2 x 1 * 3개의 합 비교 -> 더 큰걸 뽑아다가 쓴다)

n, a, b = map(int, input().split())
tile_a = sorted(list(map(int, input().split())))
tile_b = sorted(list(map(int, input().split())))
ans = 0

if n % 2:
    ans += tile_a[-1]
    tile_a.pop()
    n -= 1

for i in range(0, n, 2):
    a_val, b_val = 0, 0
    if len(tile_a) >= 2:
        a_val = tile_a[-1] + tile_a[-2]
    if len(tile_b) >= 1:
        b_val = tile_b[-1]

    if a_val > b_val:
        ans += a_val
        for j in range(2):
            tile_a.pop()
    else:
        ans += b_val
        tile_b.pop()

print(ans)