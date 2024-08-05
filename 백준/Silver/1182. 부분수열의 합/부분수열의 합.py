import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline


def dfs(idx, sub_number):
    global answer
    if sub_number == S:
        answer += 1
        # return

    for j in range(idx + 1, N):
        sub_number += numbers[j]
        dfs(j, sub_number)
        sub_number -= numbers[j]


N, S = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
answer = 0

for i in range(N):
    temp = numbers[i]
    dfs(i, temp)

print(answer)