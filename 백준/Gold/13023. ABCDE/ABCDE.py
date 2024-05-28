import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(depth, point):
    global answer
    if depth == 5:
        answer = 1
        return

    for element in friends[point]:
        if visited[element] == 0:
            visited[element] = 1
            dfs(depth + 1, element)
            visited[element] = 0


N, M = map(int, input().split())

friends = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

answer = 0

for i in range(N):
    if friends[i]:
        visited = [0 for _ in range(N)]
        visited[i] = 1
        dfs(1, i)
        if answer:
            break

print(answer)