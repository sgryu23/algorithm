import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().split())
alcohol = list(map(int, input().split()))
dq = deque()
accumulative = 0
answer = 0

for i in range(N):
    dq.append(alcohol[i])
    accumulative += alcohol[i]
    if len(dq) > L:
        accumulative -= dq.popleft()
    if 129 <= accumulative <= 138:
        answer += 1

print(answer)