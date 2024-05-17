import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())  # N: 세로줄의 개수, M: 가로줄의 개수, K: 동아리원의 수
cinema = []
answer = 0
visited = [[0 for c in range(M)] for r in range(N)]

for _ in range(N):
    cinema.append(list(input().rstrip()))

for row in range(N):
    for column in range(M - K + 1):
        i = 0
        while column + i < M and cinema[row][column + i] == '0' and visited[row][column + i] == 0:
            cinema[row][column + i] = 1
            i += 1
        if i >= K:
            answer += (i - K + 1)

print(answer)