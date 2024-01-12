import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N = int(input())
arr = [[0] * N for row in range(N)]
students = N ** 2
who_likes_whom = [[0] for zero in range(students + 1)]

for student in range(students):
    input_list = list(map(int, input().split()))
    student_num = input_list[0]  # 학생의 번호
    like_list = input_list[1:]  # student_num 학생이 좋아하는 4명의 번호
    who_likes_whom[student_num] = like_list
    checked_list = []
    for row in range(N):
        for col in range(N):
            if arr[row][col] == 0:
                likes = 0
                blank = 0
                for delta in range(4):
                    nr = row + dr[delta]
                    nc = col + dc[delta]
                    if 0 <= nr < N and 0 <= nc < N:
                        if arr[nr][nc] in like_list:
                            likes += 1
                        if arr[nr][nc] == 0:
                            blank += 1
                checked_list.append([likes, blank, row, col])

    checked_list.sort(key=lambda x: (x[0], x[1]), reverse=True)  # like_seat 큰 수대로 정렬

    if len(checked_list) > 1 and checked_list[0][0] > checked_list[1][0]:  # 1번 조건 충족
        arr[checked_list[0][2]][checked_list[0][3]] = student_num
        continue
    elif len(checked_list) == 1:
        arr[checked_list[0][2]][checked_list[0][3]] = student_num
    # 2번 조건
    max_blank = checked_list[0][1]
    for_third_condition = [[checked_list[0][2], checked_list[0][3]]]
    seat_num = 0
    saved_row = checked_list[0][2]
    saved_col = checked_list[0][3]
    flag = False
    seat = 1
    while seat < len(checked_list) and checked_list[0][1] == checked_list[seat][1]:
        if checked_list[seat][1] > max_blank:
            max_blank = checked_list[seat][1]
            saved_row, saved_col = checked_list[seat][2], checked_list[seat][3]
            seat_num = seat
            flag = False  # 인접한 칸 중에서 비어있는 칸이 하나인 경우
        elif max_blank == checked_list[seat][1]:
            flag = True  # 인접한 칸 중에서 비어있는 칸이 둘 이상인 경우
            for_third_condition.append((checked_list[seat][2], checked_list[seat][3]))
        seat += 1  # 인덱스를 하나씩 옮겨 가면서 좋아하는 학생의 수가 동일한 경우 동안 반복
    if not flag:  # 인접한 칸 중에서 비어있는 칸이 하나인 경우
        arr[saved_row][saved_col] = student_num
        continue
    row, col = for_third_condition[0][0], for_third_condition[0][1]
    arr[row][col] = student_num

# 만족도 구하기
satisfaction = 0
for row in range(N):
    for col in range(N):
        tmp_cnt = 0
        for delta in range(4):
            nr = row + dr[delta]
            nc = col + dc[delta]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] in who_likes_whom[arr[row][col]]:
                    tmp_cnt += 1
        if tmp_cnt == 1:
            satisfaction += 1
        elif tmp_cnt == 2:
            satisfaction += 10
        elif tmp_cnt == 3:
            satisfaction += 100
        elif tmp_cnt == 4:
            satisfaction += 1000

print(satisfaction)