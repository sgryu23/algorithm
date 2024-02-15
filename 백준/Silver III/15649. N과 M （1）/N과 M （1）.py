import sys
input = sys.stdin.readline


def backtracking():
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return

    for i in range(1, n + 1):
        if visited[i]:
            continue

        visited[i] = True
        answer.append(i)
        backtracking()
        answer.pop()
        visited[i] = False


n, m = map(int, input().split())
visited = [False] * (n + 1)
answer = []

backtracking()