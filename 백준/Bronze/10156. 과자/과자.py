import sys

K, N, M = map(int, sys.stdin.readline().split())

if K * N - M >= 0:
    print(K * N - M)
else:
    print(0)