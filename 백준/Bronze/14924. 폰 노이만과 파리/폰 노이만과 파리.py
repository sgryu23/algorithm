import sys
input = sys.stdin.readline

s, t, d = map(int, input().split())

time = d // (s * 2)
print(t * time)