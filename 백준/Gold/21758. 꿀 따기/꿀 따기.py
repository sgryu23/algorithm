import sys
input = sys.stdin.readline

N = int(input())
honey = list(map(int, input().split()))

answer = 0
accumulative_sum = []
accumulative_sum.append(honey[0])

for i in range(1, N):
    accumulative_sum.append(accumulative_sum[i - 1] + honey[i])

# case 1: 왼쪽 끝에 벌통이 있는 경우
for left in range(1, N - 1):
    answer = max(answer, accumulative_sum[N - 2] + accumulative_sum[left - 1] - honey[left])

# case 2: 오른쪽 끝에 벌통이 있는 경우
for right in range(1, N - 1):
    answer = max(answer, accumulative_sum[N - 1] - honey[0] - honey[right] + accumulative_sum[N - 1] - accumulative_sum[right])

# case 3: 중간에 벌통이 있는 경우
for mid in range(1, N - 1):
    answer = max(answer, accumulative_sum[N - 2] - honey[0] + honey[mid])

print(answer)