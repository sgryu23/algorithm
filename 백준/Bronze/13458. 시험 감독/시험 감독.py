import sys
input = sys.stdin.readline

n = int(input())
students = list(map(int, input().split()))
b, c = map(int, input().split())
answer = 0

for i in range(n):
    num = students[i] - b
    answer += 1
    if num > 0:
        if num % c == 0:
            answer += num // c
        else:
            answer += (num // c + 1)

print(answer)