import sys
input = sys.stdin.readline

N = int(input())
friends = list(input().split())
hellobit = input().rstrip()
answer = 0

for friend in friends:
    if friend == hellobit:
        answer += 1
print(answer)