import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline


def dfs(r, c):
    # 방문한 적이 있다면 해당 값을 그대로 사용
    if dp[r][c]:
        return dp[r][c]

    dp[r][c] = 1
    for nr, nc in [[r + 1, c], [r, c + 1], [r - 1, c], [r, c - 1]]:
        if 0 <= nr < n and 0 <= nc < n:
            # 이동할 곳에 대나무가 더 많다면
            if arr[nr][nc] > arr[r][c]:
                # dp 깊이 탐색 여부 확인 -> 0이면 아직 탐색하지 않은 곳
                dp[r][c] = max(dp[r][c], dfs(nr, nc) + 1)

    return dp[r][c]


n = int(input())  # n: 대나무 숲의 크기
arr = []
dp = [[0 for i in range(n)] for j in range(n)]
for _ in range(n):
    arr.append(list(map(int, input().split())))

answer = 0

for row in range(n):
    for column in range(n):
        if dp[row][column] == 0:
            dfs(row, column)

for k in range(n):
    answer = max(answer, max(dp[k]))

print(answer)