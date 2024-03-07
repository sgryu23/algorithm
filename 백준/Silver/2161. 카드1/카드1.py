import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

dq = deque([i for i in range(1, n + 1)])
answer = []

while len(dq) > 0:
    discard = dq.popleft()
    answer.append(discard)

    dq.rotate(-1)

print(*answer)