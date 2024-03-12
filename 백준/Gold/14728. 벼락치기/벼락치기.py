import sys
input = sys.stdin.readline

n, t = map(int, input().split())  # n: 시험 단원의 개수, t: 총 시간
estimated_time = [0]
grade = [0]

for _ in range(n):
    k, s = map(int, input().split())  # k: 예상 공부 시간, s: 문제의 배점
    estimated_time.append(k)
    grade.append(s)

dp = [[0 for c in range(t + 1)] for r in range(n + 1)]

for i in range(1, n + 1):
    _time = estimated_time[i]  # _time: 예상 시간
    _grade = grade[i]          # _grade: 그 때 받을 수 있는 점수
    for j in range(1, t + 1):
        if _time > j:
            dp[i][j] = dp[i- 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j - _time] + _grade, dp[i - 1][j])

print(dp[-1][-1])