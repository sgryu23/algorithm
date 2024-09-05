import sys
input = sys.stdin.readline

N = int(input())
answer = 0

for _ in range(N):
    input_ = input().rstrip()
    if '01' in input_ or 'OI' in input_:
        answer += 1

print(answer)