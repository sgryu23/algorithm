import sys
input = sys.stdin.readline

# ccw 알고리즘 응용
# 선의 교차 판정을 위해 점이 시계 방향에 있으면 -1, 반시계 방향에 있으면 1
# 두 결과를 곱했을 때 둘 다 -1이 나온다면 선분이 교차


def ccw(d1, d2, d3):
    a = d1[0] * d2[1] + d2[0] * d3[1] + d3[0] * d1[1]
    b = d1[1] * d2[0] + d2[1] * d3[0] + d3[1] * d1[0]

    if a - b > 0:  # 반시계 방향
        return 1
    elif a - b < 0:  # 시계 방향
        return -1
    else:
        return 0


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

dot1 = [x1, y1]
dot2 = [x2, y2]
dot3 = [x3, y3]
dot4 = [x4, y4]

val1 = ccw(dot1, dot2, dot3) * ccw(dot1, dot2, dot4)
val2 = ccw(dot3, dot4, dot1) * ccw(dot3, dot4, dot2)

if val1 == -1 and val2 == -1:
    print(1)
else:
    print(0)