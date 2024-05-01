import sys
import math
input = sys.stdin.readline

T = int(input().rstrip())

for tc in range(T):
    x, y = map(int, input().split())
    distance = y - x
    n = round(math.sqrt(float(distance)))
    while True:
        if abs(n ** 2 - distance) <= n:
            if distance <= n ** 2:
                print(2 * n - 1)
                break
            else:
                print(2 * n)
                break