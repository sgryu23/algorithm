cols, rows = map(int, input().split())      # 전체 격자 공간의 너비와 높이
s_col, s_row = map(int, input().split())    # 시작점
t = int(input())                            # 움직이는 시간
col_tmp, row_tmp = s_col + t, s_row + t
row = 0
col = 0
# 열 위치 구하기
if (col_tmp // cols) % 2 == 0:
    col_tmp = col_tmp - cols*(col_tmp//cols)
    col = col_tmp
else:
    col_tmp = col_tmp - cols*(col_tmp//cols)
    col = cols - col_tmp

# 행 위치 구하기
if (row_tmp // rows) % 2 == 0:
    row_tmp = row_tmp - rows*(row_tmp//rows)
    row = row_tmp
else:
    row_tmp = row_tmp - rows*(row_tmp//rows)
    row = rows - row_tmp

print(col,row)