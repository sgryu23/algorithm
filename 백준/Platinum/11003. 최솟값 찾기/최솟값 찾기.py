import sys
from collections import deque
input = sys.stdin.readline

n, l = map(int, input().split())
lst = list(map(int, input().split()))

dq = deque()

for i in range(n):
    # 현재 값보다 큰 값이 앞에 있으면 pop() -> 작은 값만 남긴다
    while dq and dq[-1][0] >= lst[i]:
        dq.pop()
    dq.append((lst[i], i))

    # i - L + 1 ~ i 사이의 범위만큼 조정
    if dq[0][1] <= i - l:
        dq.popleft()

    print(dq[0][0], end=" ")