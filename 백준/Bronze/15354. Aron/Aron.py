import sys
input = sys.stdin.readline

N = int(input())
answer = 1
previous = ''

for _ in range(N):
    person = input().rstrip()
    if person == previous:
        continue
    else:
        previous = person
        answer += 1

print(answer)