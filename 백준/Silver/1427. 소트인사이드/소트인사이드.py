import sys

N = list(map(int, sys.stdin.readline().rstrip()))
sorted_N = sorted(N, reverse=True)
answer = ''
for i in sorted_N:
    answer += str(i)

print(answer)