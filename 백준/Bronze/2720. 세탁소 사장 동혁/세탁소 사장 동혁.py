import sys
input = sys.stdin.readline

t = int(input())  # t: 테스트 케이스의 개수
for i in range(t):
    change = int(input())
    answer = [0, 0, 0, 0]
    while change >= 25:
        change -= 25
        answer[0] += 1

    while change >= 10:
        change -= 10
        answer[1] += 1

    while change >= 5:
        change -= 5
        answer[2] += 1

    while change > 0:
        change -= 1
        answer[3] += 1

    print(*answer)