import sys
input = sys.stdin.readline


def runway_check_row(row, col):
    # 경사로가 될 수 없는 경우
    # 1. 차이가 2 이상
    # 2. L 만큼의 여유가 있어야 함(이미 경사로를 놓은 경우 불가능)
    is_runway = [False] * N  # 경사로를 놓았는지 체크용(경사로를 놓았다면 True)
    for i in range(1, N):
        # 차이가 2 이상인 경우: False
        if abs(arr[row][i] - arr[row][i - 1]) > 1:
            return False
        if arr[row][i - 1] < arr[row][i]:  # 오른쪽이 더 큰 경우
            for j in range(L):
                # 범위를 벗어나거나 / 이미 설치했거나 / 낮은 곳의 높이가 다른 경우 -> 경사로 X
                if i - j - 1 < 0 or arr[row][i - 1] != arr[row][i - j - 1] or is_runway[i - j - 1]:
                    return False
                # 높이가 같으면 경사로 설치
                if arr[row][i - 1] == arr[row][i - j - 1]:
                    is_runway[i - j - 1] = True
        elif arr[row][i - 1] > arr[row][i]:  # 왼쪽이 더 큰 경우
            for j in range(L):
                # 범위를 벗어나거나 / 높이가 다르거나 / 이미 경사로가 설치된 경우 -> 경사로 X
                if i + j >= N or arr[row][i] != arr[row][i + j] or is_runway[i + j]:
                    return False
                if arr[row][i] == arr[row][i + j]:
                    is_runway[i + j] = True
    return 1


def runway_check_col(row, col):
    # 경사로가 될 수 없는 경우
    # 1. 차이가 2 이상
    # 2. L 만큼의 여유가 있어야 함(이미 경사로를 놓은 경우 불가능)
    is_runway = [False] * N  # 경사로를 놓았는지 체크용(경사로를 놓았다면 True)
    for i in range(1, N):
        # 차이가 2 이상인 경우: False
        if abs(arr[i][col] - arr[i - 1][col]) > 1:
            return False
        if arr[i - 1][col] < arr[i][col]:  # 아래쪽이 더 큰 경우: 위로 L만큼 가면서 확인
            for j in range(L):
                # 범위를 벗어나거나 / 이미 설치했거나 / 낮은 곳의 높이가 다른 경우 -> 경사로 X
                if i - j - 1 < 0 or arr[i - 1][col] != arr[i - j - 1][col] or is_runway[i - j - 1]:
                    return False
                # 높이가 같으면 경사로 설치
                if arr[i - 1][col] == arr[i - j - 1][col]:
                    is_runway[i - j - 1] = True
        elif arr[i - 1][col] > arr[i][col]:  # 위쪽이 더 큰 경우: 아래로 L만큼 가면서 확인
            for j in range(L):
                # 범위를 벗어나거나 / 높이가 다르거나 / 이미 경사로가 설치된 경우 -> 경사로 X
                if i + j >= N or arr[i][col] != arr[i + j][col] or is_runway[i + j]:
                    return False
                if arr[i][col] == arr[i + j][col]:
                    is_runway[i + j] = True
    return 1


N, L = map(int, input().split())  # N: 배열 길이, L: 경사로의 길이
arr = []
for _ in range(N):
    arr.append(list(map(int, input().rstrip().split())))

cnt = 0
for i in range(N):
    cnt += runway_check_row(i, 0)
    # print(f'{i}행 탐구: {cnt}')  # 디버깅용
    cnt += runway_check_col(0, i)
    # print(f'{i}열 탐구: {cnt}')  # 디버깅용
print(cnt)