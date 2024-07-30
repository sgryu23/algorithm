import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = deque([i for i in range(1, N + 1)])
answer_candidate = list(map(int, input().split()))
answer = 0

for number in answer_candidate:
    while True:
        if numbers[0] == number:
            numbers.popleft()
            break
        if numbers.index(number) < len(numbers) / 2:
            while numbers[0] != number:
                numbers.append(numbers.popleft())
                answer += 1
        else:
            while numbers[0] != number:
                numbers.appendleft(numbers.pop())
                answer += 1

print(answer)