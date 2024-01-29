from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def solution(board):
    column = len(board[0])
    row = len(board)
    visited = [[10000 for i in range(column)] for j in range(row)]
    queue = deque()
    # 로봇의 처음 위치를 찾아서 queue 에 append
    for r in range(row):
        for c in range(column):
            if board[r][c] == 'R':    
                queue.append((r, c, 0))
        if queue:
            break
    
    while queue:
        x, y, cnt = queue.popleft()
        
        if board[x][y] == 'G':
            return cnt
        
        for k in range(4):
            nx, ny = x, y
                        
            while 0 <= nx + dr[k] < row and 0 <= ny + dc[k] < column and board[nx + dr[k]][ny + dc[k]] != 'D':
                nx += dr[k]
                ny += dc[k]
            
            if visited[nx][ny] > cnt + 1:
                visited[nx][ny] = cnt + 1
                queue.append((nx, ny, cnt + 1))
    
    return -1