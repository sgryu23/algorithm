import sys
input = sys.stdin.readline


def ccw(dot1, dot2, dot3):
    x1, y1 = dot1
    x2, y2 = dot2
    x3, y3 = dot3
    s = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if s > 0:
        return True
    else:
        return False


n, px, py = map(int, input().split())
pxy = (px, py)
dots = []

for _ in range(n):
    dots.append(tuple(map(int, input().split())))

is_convex_hull = True
answer = 0

while is_convex_hull and len(dots) > 2:
    dots.sort()   # 좌표 정렬(반시계방향)
    b_convex_hull, t_convex_hull = [], []
    b_convex_hull.append(dots[0])
    b_convex_hull.append(dots[1])

    for i in range(2, n):
        b_convex_hull.append(dots[i])
        flag = True
        while flag and len(b_convex_hull) > 2:
            dot_1 = b_convex_hull.pop()
            dot_2 = b_convex_hull.pop()

            if ccw(b_convex_hull[-1], dot_2, dot_1):
                b_convex_hull.append(dot_2)
                b_convex_hull.append(dot_1)
                flag = False
            else:
                b_convex_hull.append(dot_1)

    t_convex_hull.append(dots[-1])
    t_convex_hull.append(dots[-2])

    for j in range(n - 3, -1, -1):
        t_convex_hull.append(dots[j])
        flag = True
        while flag and len(t_convex_hull) > 2:
            dot1_ = t_convex_hull.pop()
            dot2_ = t_convex_hull.pop()

            if ccw(t_convex_hull[-1], dot2_, dot1_):
                t_convex_hull.append(dot2_)
                t_convex_hull.append(dot1_)
                flag = False
            else:
                t_convex_hull.append(dot1_)

    b_convex_hull.pop()
    convex_hull = b_convex_hull + t_convex_hull
    dots = list(set(dots) - set(convex_hull))
    n = len(dots)

    for k in range(len(convex_hull) - 1):
        if not ccw(convex_hull[k], convex_hull[k + 1], pxy):
            is_convex_hull = False
            break

    if is_convex_hull:
        answer += 1

print(answer)