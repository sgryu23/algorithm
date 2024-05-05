import sys
input = sys.stdin.readline


def dfs(depth):
    global answer
    if depth == M:
        print(*answer)
        return

    for i in range(N):
        answer.append(numbers[i])
        dfs(depth + 1)
        answer.pop()


N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
answer = []

for j in range(N):
    answer.append(numbers[j])
    dfs(1)
    answer.pop()