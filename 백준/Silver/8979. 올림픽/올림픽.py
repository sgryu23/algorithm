import sys
input = sys.stdin.readline

N, K = map(int, input().split())  # N: 국가의 수, K: 등수를 알고 싶은 국가

countries = []
for _ in range(N):
    countries.append(list(map(int, input().split())))

countries.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

ranking, cumulative = 1, 0

for i in range(1, N):
    if countries[i - 1][1:] == countries[i][1:]:
        cumulative += 1
    else:
        if cumulative:
            ranking += cumulative
            cumulative = 0
        ranking += 1
    if countries[i][0] == K:
        print(ranking)
        break