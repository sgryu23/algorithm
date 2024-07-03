import sys
input = sys.stdin.readline

N = int(input())
li = []

for _ in range(N):
    li.append(int(input()))

li.sort(reverse=True)

for i in range(N):
    print(li[i])