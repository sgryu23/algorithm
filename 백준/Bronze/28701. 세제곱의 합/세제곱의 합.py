import sys
N = int(sys.stdin.readline())
answer = 0

for i in range(1, N + 1):
    answer += i

print(answer)
print(answer ** 2)

answer = 0

for j in range(1, N + 1):
    answer += j ** 3

print(answer)