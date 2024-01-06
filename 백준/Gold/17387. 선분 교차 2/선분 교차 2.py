import sys
input = sys.stdin.readline

# ccw 알고리즘 응용(17386 선분 교차 1에서 조건이 추가된 문제)
# 17386에서 쓴 방법과는 조금 다르게 풀었다. (ccw 함수)


def ccw(x1, y1, x2, y2, x3, y3):
    val = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)

    if val > 0:  # 반시계 방향
        return 1
    elif val < 0:  # 시계 방향
        return -1
    else:   # 일직선 위에 있는 경우
        return 0


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

ans = 0

if ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) == 0 and ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) == 0:
    if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
        ans = 1
elif ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) <= 0 and ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) <= 0:
    ans = 1

print(ans)