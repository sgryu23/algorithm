import sys
input = sys.stdin.readline

N, M = map(int, input().split())
sequence = list(map(int, input().split()))
answer = 0
result = 0
left = right = 0

while right < N:
    if sum(sequence[left: right + 1]) == M:
        answer += 1
        left += 1
        right += 1
    elif sum(sequence[left: right + 1]) > M:
        left += 1
        if left > right:
            # if sequence[left] == M:
            #     answer += 1
            right += 1
    else:
        right += 1

print(answer)