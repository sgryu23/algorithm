import sys

li = sorted(list(map(int, sys.stdin.readline().split())))
for i in range(3):
    print(li[i], end=' ')