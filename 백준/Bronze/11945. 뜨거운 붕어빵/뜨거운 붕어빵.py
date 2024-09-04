import sys

N, M = map(int, input().split())

for _ in range(N):
    i = sys.stdin.readline().rstrip()
    line = ''
    for j in i:
        line = j + line
    print(line)