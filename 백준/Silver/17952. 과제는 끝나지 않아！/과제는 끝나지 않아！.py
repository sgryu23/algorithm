import sys
input = sys.stdin.readline

N = int(input())

homeworks = []
answer = 0

for _ in range(N):
    li = list(map(int, input().split()))
    if li[0] == 0:
        if homeworks:
            grade, time = homeworks.pop()
            time -= 1
            if time <= 0:
                answer += grade
            else:
                homeworks.append([grade, time])
    else:
        if li[2] == 1:
            answer += li[1]
        else:
            homeworks.append([li[1], li[2] - 1])

print(answer)