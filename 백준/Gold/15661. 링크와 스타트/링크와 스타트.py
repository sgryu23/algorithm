import sys
input = sys.stdin.readline


def calc_power(arr):
    result = 0
    for row in arr:
        for col in arr:
            result += team[row][col]
    return result


def build_team(num):
    start, link = [], []
    for j in range(n):
        # i == 0 은 start, 1이면 link 팀
        if (num & (1 << j)) == 0:
            start.append(j)
        else:
            link.append(j)
    return abs(calc_power(start) - calc_power(link))


n = int(input())  # n: 줄의 수
team = []
for _ in range(n):
    team.append(list(map(int, input().split())))

min_val = sys.maxsize
for i in range(1, (1 << n) - 1):
    min_val = min(min_val, build_team(i))

print(min_val)