import sys
input = sys.stdin.readline

for _ in range(4):
    r1, c1, r2, c2, r3, c3, r4, c4 = map(int, input().split())
    # a인 경우는 많으니까 else로 두고 b, c, d를 판별하자
    # d: 겹치지 않는 경우
    if r1 > r4 or c1 > c4 or r3 > r2 or c3 > c2:
        print('d')
        continue
    # b, c: 선분끼리 겹치는 경우, 점만 접하는 경우
    if r1 == r4 or r2 == r3:
        # c인 경우
        if c1 == c4 or c2 == c3:
            print('c')
            continue
        # b인 경우
        else:
            print('b')
            continue
    elif c2 == c3 or c1 == c4:
        print('b')
        continue

    # a: 겹치는 경우
    else:
        print('a')

# import sys
# input = sys.stdin.readline
#
# for _ in range(4):
#     r1, c1, r2, c2, r3, c3, r4, c4 = map(int, input().split())
#     # a인 경우는 많으니까 else로 두고 b, c, d를 판별하자
#     # b: 선분끼리 겹치는 경우
#     if (r1 == r4 and (c1 < c3 < c2 or c1 < c4 < c2)) or (r2 == r3 and (c1 < c3 < c2 or c1 < c3 < c2)):
#         print('b')
#         continue
#     elif (c1 == c4 and (r1 < r3 < r2 or r1 < r4 < r2)) or (c2 == c3 and (r1 < r3 < r2 or r1 < r4 < r2)):
#         print('b')
#         continue
#     # c: 점만 만나는 경우
#     elif (r1 == r4 and c2 == c3) or (r1 == r4 and c1 == c4) or (r2 == r3 and c1 == c4) or (r2 == r3 and c2 ==c3):
#         print('c')
#         continue
#     # d: 겹치는 곳이 없는 경우
#     elif r1 > r4 or c1 > c4 or r3 > r2 or c3 > c2:
#         print('d')
#         continue
#     else:
#         print('a')


# 틀렸습니다. (다섯 번이나 틀림..)
# for _ in range(4):
#     x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
#     # x2, y2 & x3, y3 비교
#     if x1 <= x3 < x2:
#         # y2 가 y3 보다 클 때(직사각형)
#         if y1 <= y3 < y2 or y1 < y4 <= y2:
#             print('a')
#         elif y3 < y1 and y4 > y2:
#             print('a')
#         # y 좌표가 같을 때(선)
#         elif y2 == y3 or y1 == y4:
#             print('b')
#         # 3. 겹치지 않을 때
#         else:
#             print('d')
#     elif x2 == x3:
#         # y2 가 y3 보다 클 때(선분)
#         if y1 <= y3 < y2:
#             print('b')
#         # y 좌표도 같을 때(점)
#         elif y2 == y3:
#             print('c')
#         # 3. 겹치지 않을 때
#         else:
#             print('d')
#
#     # x1, y1 & x4, y4 비교
#     elif x1 < x4 <= x2:
#         # y1 가 y4 보다 클 때(직사각형)
#         if y1 < y4 <= y2 or y1 <= y3 < y2:
#             print('a')
#         elif y3 < y1 and y4 > y2:
#             print('a')
#         # y 좌표가 같을 때(선)
#         elif y1 == y4 or y2 == y3:
#             print('b')
#         # 3. 겹치지 않을 때
#         else:
#             print('d')
#     elif x4 == x1:
#         # y4 가 y1 보다 클 때(선분)
#         if y1 < y4 <= y2:
#             print('b')
#         # y 좌표도 같을 때(점)
#         elif y4 == y1:
#             print('c')
#         # 3. 겹치지 않을 때
#         else:
#             print('d')
#     # 위에서 아무 것도 걸리지 않았을 때(겹치지 않음)
#     else:
#         print('d')

# 실패한 코드(메모리 초과)
# import sys
# sys.stdin = open('input_2527.txt')
#
# blank_list = [[0] * 50000 for _ in range(50000)]               # 빈 리스트 생성 -> 메모리 초과 뜬다.
#
# for _ in range(4):
#     arr = list(map(int, input().split()))
#     r1_x, r1_y, r1_p, r1_q = arr[0], arr[1], arr[2], arr[3]    # 첫 직사각형 좌표 배정
#     r2_x, r2_y, r2_p, r2_q = arr[4], arr[5], arr[6], arr[7]    # 두 번째 직사각형 좌표 배정
#     overlap_x = set()                                                      # 겹치는 x 좌표를 담기 위한 세트(중복이면 삭제하려고)
#     overlap_y = set()                                                      # 겹치는 y 좌표를 담기 위한 세트
#     for row_r1 in range(r1_y, r1_q+1):                             # 첫 번째 직사각형의 범위를 1씩 더해준다.
#         for col_r1 in range(r1_x, r1_p+1):
#             blank_list[row_r1][col_r1] += 1
#     for row_r2 in range(r2_y, r2_q+1):
#         for col_r2 in range(r2_x, r2_p+1):
#             blank_list[row_r2][col_r2] += 1
#     # 구간을 돌면서 2가 있는지 체크
#     for check_row in range(min(r1_y, r2_y), max(r1_q, r2_q)):
#         for check_col in range(min(r1_x, r2_x), max(r1_p, r2_p)):
#             if blank_list[check_row][check_col] == 2:
#                 overlap_x.add(check_col)
#                 overlap_y.add(check_row)
#     if len(overlap_x) > 0 or len(overlap_y) > 0:
#         if len(overlap_x) == 1 and len(overlap_y) == 1:
#             print('c')
#         elif len(overlap_x) == 1 and len(overlap_y) > 1:
#             print('b')
#         elif len(overlap_x) > 1 and len(overlap_y) == 1:
#             print('b')
#         else:
#             print('a')
#     else:
#         print('d')