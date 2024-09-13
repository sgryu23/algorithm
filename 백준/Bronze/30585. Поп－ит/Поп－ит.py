import sys
input = sys.stdin.readline

h, w = map(int, input().split())

arr = []

for _ in range(h):
    arr.append(list(input().rstrip()))

true = 0

for r in range(h):
    for c in range(w):
        if arr[r][c] == '1':
            true += 1

if (h * w) // 2 >= true:
    print(true)
else:
    print(h * w - true)