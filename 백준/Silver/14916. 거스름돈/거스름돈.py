import sys
input = sys.stdin.readline

n = int(input())
answer = 0

while True:
    if n % 5 == 0:
        answer += n // 5
        print(answer)
        break
    else:
        n -= 2
        answer += 1

    if n < 0:
        print(-1)
        break
    elif n == 0:
        print(answer)
        break