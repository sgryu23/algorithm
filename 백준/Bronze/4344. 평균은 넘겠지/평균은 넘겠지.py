import sys
input = sys.stdin.readline

c = int(input())
for testcase in range(c):
    input_list = list(map(int, input().split()))
    total_number = input_list[0]
    average_grade = (sum(input_list) - total_number) / total_number
    above_average = 0
    for student in range(1, total_number + 1):
        if input_list[student] > average_grade:
            above_average += 1
    answer = str(round(above_average * 100 / total_number, 3))
    if len(answer) < 6:
        answer += (6 - len(answer)) * '0'
    print(answer + '%')