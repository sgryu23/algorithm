import sys
input = sys.stdin.readline

N, K = map(int, input().split())  # N: 국가의 수, K: 등수를 알고 싶은 국가

countries = []
for _ in range(N):
    countries.append(list(map(int, input().split())))

countries.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

for i in range(N):
    if countries[i][0] == K:
        idx = i

for j in range(N):
    if countries[idx][1:] == countries[j][1:]:
        print(j + 1)
        break