import sys

N, T, C, P = map(int, sys.stdin.readline().split())  # N: 여름 일수, T: 스타후르츠가 자라는데 걸리는 일수, C: 스타후르츠 심을 수 있는 칸 수, P: 하나의 가격

temp = (N - 1) // T
answer = temp * C * P
print(answer)