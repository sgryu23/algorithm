import sys
input = sys.stdin.readline

# 아이디어 정리
# 이중 for 문으로 돌면서 각 dp의 자리에 최댓값 저장하기; 시간 초과남
# 이전 값을 더해주면서 이전 값보다 크면 저장

n = int(input())
sequence = list(map(int, input().split()))
for i in range(1, n):
    sequence[i] = max(sequence[i], sequence[i] + sequence[i - 1])
# print(sequence)
print(max(sequence))