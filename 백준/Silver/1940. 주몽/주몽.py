import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
materials = sorted(list(map(int, input().split())))

answer = 0
left, right = 0, N - 1

while left < right:
    if materials[left] + materials[right] == M:
        answer += 1
        left += 1
    elif materials[left] + materials[right] < M:
        left += 1
    elif materials[left] + materials[right] > M:
        right -= 1

print(answer)