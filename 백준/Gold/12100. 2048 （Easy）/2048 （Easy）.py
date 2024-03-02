import sys
input = sys.stdin.readline


def up(arr):
    up_board = [[0 for c in range(n)] for r in range(n)]
    for col in range(n):
        saved_value = -1
        idx = 0
        flag = False
        for row in range(n):
            # 현재 값이 0이 아닐 때
            if arr[row][col] != 0:
                # 저장된 값이 없으면
                if not flag:
                    saved_value = arr[row][col]  # 해당 위치의 값을 저장해줌
                    flag = True
                # 저장된 값이 있으면
                else:
                    # 값이 같으면 합침
                    if saved_value == arr[row][col]:
                        up_board[idx][col] = saved_value * 2
                        saved_value = -1
                        flag = False
                    else:
                        up_board[idx][col] = saved_value
                        saved_value = arr[row][col]
                    idx += 1
        # 탐색 후 값이 남아 있다면
        if saved_value != -1:
            # 새 보드 인덱스에 저장
            up_board[idx][col] = saved_value

    return up_board


def down(arr):
    down_board = [[0 for c in range(n)] for r in range(n)]
    for col in range(n):
        saved_value = -1
        idx = n - 1
        flag = False
        for row in range(n - 1, -1, -1):
            # 현재 값이 0이 아닐 때
            if arr[row][col] != 0:
                # 저장된 값이 없으면
                if not flag:
                    saved_value = arr[row][col]  # 해당 위치의 값을 저장해줌
                    flag = True
                # 저장된 값이 있으면
                else:
                    # 값이 같으면 합침
                    if saved_value == arr[row][col]:
                        down_board[idx][col] = saved_value * 2
                        saved_value = -1
                        flag = False
                    else:
                        down_board[idx][col] = saved_value
                        saved_value = arr[row][col]
                    idx -= 1
        # 탐색 후 값이 남아 있다면
        if saved_value != -1:
            # 새 보드 인덱스에 저장
            down_board[idx][col] = saved_value
    return down_board


def right(arr):
    right_board = [[0 for c in range(n)] for r in range(n)]
    for row in range(n):
        saved_value = -1
        idx = n - 1
        flag = False
        for col in range(n - 1, -1, -1):
            if arr[row][col] != 0:
                if not flag:
                    saved_value = arr[row][col]
                    flag = True
                else:
                    if saved_value == arr[row][col]:
                        right_board[row][idx] = saved_value * 2
                        saved_value = -1
                        flag = False
                    else:
                        right_board[row][idx] = saved_value
                        saved_value = arr[row][col]
                    idx -= 1
        # 탐색 후 값이 남이 있으면
        if saved_value != -1:
            right_board[row][idx] = saved_value

    return right_board


def left(arr):
    left_board = [[0 for c in range(n)] for r in range(n)]
    for row in range(n):
        saved_value = -1
        idx = 0
        flag = False
        for col in range(n):
            if arr[row][col] != 0:
                if not flag:
                    saved_value = arr[row][col]
                    flag = True
                else:
                    if saved_value == arr[row][col]:
                        left_board[row][idx] = saved_value * 2
                        saved_value = -1
                        flag = False
                    else:
                        left_board[row][idx] = saved_value
                        saved_value = arr[row][col]
                    idx += 1
        # 탐색 후 값이 남아 있으면
        if saved_value != -1:
            left_board[row][idx] = saved_value

    return left_board


def dfs(arr, num):
    global answer
    if num == 5:
        for row in range(n):
            answer = max(answer, max(arr[row]))
        return
    board_copy = up(arr)
    dfs(board_copy, num + 1)
    board_copy = down(arr)
    dfs(board_copy, num + 1)
    board_copy = right(arr)
    dfs(board_copy, num + 1)
    board_copy = left(arr)
    dfs(board_copy, num + 1)


n = int(input())  # n: 보드 한 변의 길이
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

answer = 0
dfs(board, 0)
print(answer)