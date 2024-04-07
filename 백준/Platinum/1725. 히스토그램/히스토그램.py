import sys
input = sys.stdin.readline

N = int(input())  # N: 주어지는 입력 값의 개수
answer = 0
li = []
for _ in range(N):
    li.append(int(input()))

stack = []
for i in range(N):
    idx = i
    while stack and stack[-1][1] > li[i]:
        idx, height = stack.pop()
        # 현재 인덱스와 해당 인덱스까지의 차이와 높이를 곱해서 최대 넓이를 탐색
        rst = (i - idx) * height
        answer = max(answer, rst)
    stack.append([idx, li[i]])

while stack:
    idx, height = stack.pop()
    rst = (N - idx) * height
    answer = max(answer, rst)

print(answer)