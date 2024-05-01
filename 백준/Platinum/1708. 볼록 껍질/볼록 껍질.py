import sys
input = sys.stdin.readline


def inclination(d1, d2):
    return d2[0] - d1[0], d2[1] - d1[1]


def ccw(dot1, dot2, dot3):
    v, u = inclination(dot1, dot2), inclination(dot2, dot3)
    if v[0] * u[1] > v[1] * u[0]:
        return True
    return False


def convex_hull(li):
    convex = []
    for p3 in li:
        while len(convex) >= 2:
            p1, p2 = convex[-2], convex[-1]
            if ccw(p1, p2, p3):
                break
            convex.pop()
        convex.append(p3)

    return len(convex)


n = int(input())
answer = -2
positions = []

for i in range(n):
    positions.append(list(map(int, input().split())))

positions.sort(key=lambda x: (x[0], x[1]))
answer += convex_hull(positions)

positions.reverse()
answer += convex_hull(positions)
print(answer)