import sys

A, B, C = map(int, sys.stdin.readline().split())

if C - B <= 0:
    print(-1)
else:
    profit = int((A / (C - B)))
    answer = profit + 1
    print(answer)