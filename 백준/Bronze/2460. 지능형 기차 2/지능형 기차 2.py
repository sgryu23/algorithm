import sys
input = sys.stdin.readline

train = 0
answer = 0

for _ in range(10):
    go, come = map(int, input().split())
    train -= go
    train += come
    answer = max(train, answer)

print(answer)