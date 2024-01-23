import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lines = []
for line in range(k):
    lines.append(int(input()))

left, right = 1, max(lines)

while left <= right:
    mid = (left + right) // 2
    cnt = sum(line // mid for line in lines)
    if cnt < n:
        right = mid - 1
    else:
        left = mid + 1

print(right)