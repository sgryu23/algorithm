import sys
input = sys.stdin.readline

N = int(input())  # N: 수의 개수
numbers = list(map(int, input().split()))
M = int(input())
memory = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    memory[i] = memory[i - 1] + numbers[i - 1]

for _ in range(M):
    start, end = map(int, input().split())
    print(memory[end] - memory[start - 1])