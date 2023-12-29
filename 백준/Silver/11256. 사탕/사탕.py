import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    J, N = map(int, input().split())
    boxes = []
    for n in range(N):
        R, C = map(int, input().split())
        boxes.append(R * C)
    boxes.sort(reverse=True)
    idx = 0
    while J > 0:
        J -= boxes[idx]
        idx += 1
    print(idx)