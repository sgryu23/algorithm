import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    answer = 0
    for i in range(n, -1, -1):
        answer += i
    print(answer)