import sys
input = sys.stdin.readline

n, m = map(int, input().split())
baskets = [i for i in range(n + 1)]

for j in range(m):
    a, b = map(int, input().split())
    baskets[a], baskets[b] = baskets[b], baskets[a]

for k in range(1, n + 1):
    print(baskets[k], end=' ')