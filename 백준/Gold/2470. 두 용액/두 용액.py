import sys
input = sys.stdin.readline

N = int(input())  # N: 용액의 개수
fluids = sorted(list(map(int, input().split())))

left, right = 0, N - 1
answer_small, answer_big = -1000000001, 1000000001
mixed = sys.maxsize

while left < right:
    if abs(fluids[left] + fluids[right]) < mixed:
        answer_small, answer_big = fluids[left], fluids[right]
        mixed = abs(fluids[left] + fluids[right])

    if fluids[left] + fluids[right] >= 0:
        right -= 1
    else:
        left += 1

print(answer_small, answer_big)