import sys
from collections import deque
input = sys.stdin.readline

t = int(input())  # t: 테스트 케이스 개수
for test in range(t):
    n = int(input())  # n: 편의점 개수
    visited = [False] * (n + 1)
    conv = []
    sg_r, sg_c = map(int, input().split())  # sg_r, sg_c: 상근이네 집
    for c in range(n):
        conv_r, conv_c = map(int, input().split())  # conv_r, conv_c: 편의점
        conv.append([conv_r, conv_c])
    des_r, des_c = map(int, input().split())  # des_r, des_c: 락 페스티벌 좌표
    conv.append([des_r, des_c])

    dq = deque()

    for i in range(len(conv)):
        if abs(sg_r - conv[i][0]) + abs(sg_c - conv[i][1]) <= 1000:
            dq.append(conv[i])
            visited[i] = True

    while dq:
        now_r, now_c = dq.popleft()
        for j in range(len(conv)):
            if abs(now_r - conv[j][0]) + abs(now_c - conv[j][1]) <= 1000 and not visited[j]:
                dq.append(conv[j])
                visited[j] = True

    if visited[n]:
        print('happy')
    else:
        print('sad')