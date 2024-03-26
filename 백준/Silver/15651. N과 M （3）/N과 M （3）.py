import sys
input = sys.stdin.readline


def dfs(stack):
    if len(stack) == M:
        print(*stack)
        return

    for i in range(1, N + 1):
        stack.append(i)
        dfs(stack)
        stack.pop()


N, M = map(int, input().split())
dfs([])