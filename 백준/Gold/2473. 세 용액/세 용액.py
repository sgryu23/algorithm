import sys
input = sys.stdin.readline

n = int(input())  # n: 전체 용액의 수
fluids = list(map(int, input().split()))

fluids.sort()

max_sum = 5000000000000

for i in range(n - 2):
    left, right = i + 1, n - 1

    while left < right:
        fluids_sum = fluids[i] + fluids[left] + fluids[right]

        if max_sum > abs(fluids_sum):
            max_sum = abs(fluids_sum)
            answer = [fluids[i], fluids[left], fluids[right]]

        if fluids_sum < 0:
            left += 1
        elif fluids_sum > 0:
            right -= 1
        else:
            break

print(*answer)