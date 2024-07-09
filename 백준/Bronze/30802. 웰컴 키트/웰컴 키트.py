import sys
input = sys.stdin.readline

N = int(input())
shirts = list(map(int, input().split()))
T, P = map(int, input().split())
t_shirt = 0

for i in range(6):
    t_shirt += shirts[i] // T
    if shirts[i] % T != 0:
        t_shirt += 1

print(t_shirt)
print(N // P, N % P)