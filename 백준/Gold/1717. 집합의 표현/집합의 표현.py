import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n + 1)]


def find_parent(n):
    if parent[n] != n:
        parent[n] = find_parent(parent[n])
    return parent[n]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(m):
    command, a, b = map(int, input().split())
    if command:
        if find_parent(a) == find_parent(b):
            print('YES')
        else:
            print('NO')
    else:
        union_parent(a, b)