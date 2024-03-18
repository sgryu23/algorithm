import sys
input = sys.stdin.readline

x, y = map(int, input().split())
z = y * 100 // x

if z >= 99:
    print(-1)
else:
    left, right = 1, 10 ** 9

    while left <= right:
        mid = (left + right) // 2
        if (y + mid) * 100 // (x + mid) > z:
            right = mid - 1
        else:
            left = mid + 1

    print(left)