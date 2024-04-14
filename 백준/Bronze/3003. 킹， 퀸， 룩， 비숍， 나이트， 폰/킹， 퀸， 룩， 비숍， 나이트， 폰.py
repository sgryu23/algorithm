import sys
input = sys.stdin.readline

original_set = [1, 1, 2, 2, 2, 8]
input_set = list(map(int, input().split()))

for i in range(6):
    answer = original_set[i] - input_set[i]
    print(answer, end=' ')