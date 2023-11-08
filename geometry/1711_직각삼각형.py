import sys
input = sys.stdin.readline

N = int(input())
vertex = [tuple(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N - 2):
    for j in range(i+1, N - 1):
        for k in range(j+1, N):
            point1, point2, point3 = vertex[i], vertex[j], vertex[k]
            # 각 변의 길이 구하기
            side1 = (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
            side2 = (point2[0] - point3[0]) ** 2 + (point2[1] - point3[1]) ** 2
            side3 = (point3[0] - point1[0]) ** 2 + (point3[1] - point1[1]) ** 2
            # 피타고라스 정리(두 변 제곱의 합 == 빗변 제곱의 합 -> 빗변이 뭔지 모른다)
            if max(side1, side2, side3) * 2 == side1 + side2 + side3:
                ans += 1
print(ans)