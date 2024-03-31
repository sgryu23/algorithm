import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # N: 행, M: 열
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

# 첫 번째 row
for i in range(1, M):
    arr[0][i] += arr[0][i - 1]

# 좌측, 우측 각각의 방향에서 오는 경우에서 값을 비교 후 max 값 넣기
for row in range(1, N):
    dp_left = [arr[row][j] + arr[row - 1][j] for j in range(M)]
    dp_right = [arr[row][j] + arr[row - 1][j] for j in range(M)]

    # 왼쪽으로 이동할 때의 최댓값 갱신
    for col in range(1, M):
        # 기존의 자리에 있는 값과 (왼쪽 + arr 현재 좌표 값)을 비교 -> 큰 값으로 갱신
        dp_left[col] = max(dp_left[col], dp_left[col - 1] + arr[row][col])

    for col in range(M - 2, -1, -1):
        dp_right[col] = max(dp_right[col], dp_right[col + 1] + arr[row][col])

    for col in range(M):
        arr[row][col] = max(dp_left[col], dp_right[col])

print(arr[-1][-1])