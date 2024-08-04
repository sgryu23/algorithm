import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
balloons = deque(enumerate(map(int, input().split())))
answer = []

while balloons:
    idx, target = balloons.popleft()
    answer.append(idx + 1)

    if target > 0:
        balloons.rotate(-(target - 1))
    elif target < 0:
        balloons.rotate(-target)

for j in range(N):
    print(answer[j], end=' ')