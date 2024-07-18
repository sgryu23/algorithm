import sys
input = sys.stdin.readline


def gcd(k, l):
    while l:
        mod = l
        l = k % l
        k = mod
    return k


n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    print(a * b // gcd(a, b))