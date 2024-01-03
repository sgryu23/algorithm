import sys
input = sys.stdin.readline

N = int(input())
fluids = list(map(int, input().split()))
left, right = 0, N - 1
min_val = abs(fluids[left] + fluids[right])  # 최댓값은 10억(1e9)

while left < right:
    now_val = fluids[left] + fluids[right]

    if abs(now_val) <= min_val:
        min_val = abs(now_val)
        left_val = fluids[left]
        right_val = fluids[right]

    if now_val <= 0:
        left += 1
    else:
        right -= 1


print(left_val, right_val)