import sys

N, K = map(int, sys.stdin.readline().split())

visited = [0 for _ in range(N + 1)]
now = 0

for i in range(2, N + 1):
    if visited[i] == 0:
        for j in range(i, N + 1, i):
            if visited[j] == 0:
                now += 1
                visited[j] = 1
                if now == K:
                    print(j)
                    quit()