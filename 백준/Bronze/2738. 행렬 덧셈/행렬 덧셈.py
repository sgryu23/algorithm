import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [[0 for _ in range(M)] for _ in range(N)]

for _ in range(2):
    for i in range(N):
        for_append = list(map(int, input().split()))
        for j in range(M):
            A[i][j] += for_append[j]

for l in range(N):
    print(*A[l])