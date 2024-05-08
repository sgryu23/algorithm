import sys
input = sys.stdin.readline

N = int(input())
li = sorted(list(set(map(int, input().split()))))

for e in li:
    print(e, end=' ')