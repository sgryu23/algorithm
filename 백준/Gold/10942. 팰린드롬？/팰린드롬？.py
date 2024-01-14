import sys
input = sys.stdin.readline

n = int(input())  # n: 수열의 크기
numbers = list(map(int, input().split()))  # numbers: 팰린드롬 판단 수

dp = [[0] * n for _ in range(n)]
# 길이가 1인 팰린드롬 수: 대각선
for cross in range(n):
    dp[cross][cross] = 1
# 길이가 2인 팰린드롬 수: 두 숫자가 같은 경우
for check in range(n - 1):
    if numbers[check] == numbers[check + 1]:
        dp[check][check + 1] = 1
    else:
        dp[check][check + 1] = 0
# 길이가 3 이상인 경우
for row in range(n - 2):
    for col in range(n - 2 - row):
        is_palindrome = row + 2 + col
        if numbers[col] == numbers[is_palindrome] and dp[col + 1][is_palindrome - 1] == 1:
            dp[col][is_palindrome] = 1

questions = int(input())
for m in range(questions):
    start, end = map(int, input().split())
    print(dp[start - 1][end - 1])