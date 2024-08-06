import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # N: 아이스크림 종류의 수, M: 섞어 먹으면 안 되는 조합의 개수
could_mix = [[1 for c in range(N)] for r in range(N)]

for _ in range(M):
    ice_1, ice_2 = map(int, input().split())
    could_mix[ice_1 - 1][ice_2 - 1] = 0
    could_mix[ice_2 - 1][ice_1 - 1] = 0

answer = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if could_mix[i][j] and could_mix[i][k] and could_mix[j][k]:
                answer += 1

print(answer)