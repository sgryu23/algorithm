import sys
input = sys.stdin.readline

N = int(input())
answer = 0
record = [0 for _ in range(200001)]

for i in range(N):
    a, b = map(int, input().split())
    if b == 1:
        if record[a] == 0:
            record[a] += 1
        else:
            answer += 1
    elif b == 0:
        if record[a] == 0:
            answer += 1
        else:
            record[a] -= 1

answer += sum(record)
print(answer)