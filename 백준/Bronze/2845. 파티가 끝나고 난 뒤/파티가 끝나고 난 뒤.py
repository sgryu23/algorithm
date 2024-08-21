import sys
input = sys.stdin.readline

L, P = map(int, input().split())
people = list(map(int, input().split()))
authentic = L * P

for p in people:
    print(p - authentic, end=' ')