import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    cnt = 0
    x1, y1, x2, y2 = map(int, input().split())
    planets = int(input())
    for planet in range(planets):
        cx, cy, r = map(int, input().split())
        d1 = (x1 - cx) ** 2 + (y1 - cy) ** 2
        d2 = (x2 - cx) ** 2 + (y2 - cy) ** 2
        if (d1 < r ** 2 and d2 > r ** 2) or (d1 > r ** 2 and d2 < r ** 2):
            cnt += 1
    print(cnt)