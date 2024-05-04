import sys
input = sys.stdin.readline

M = int(input())  # M: 쿼리의 개수
total_sum = 0
xor_sum = 0

for _ in range(M):
    input_list = list(map(int, input().split()))
    if input_list[0] == 1:
        total_sum += input_list[1]
        xor_sum = xor_sum^input_list[1]
    elif input_list[0] == 2:
        total_sum -= input_list[1]
        xor_sum = xor_sum^input_list[1]
    elif input_list[0] == 3:
        print(total_sum)
    elif input_list[0] == 4:
        print(xor_sum)