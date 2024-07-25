import sys
input = sys.stdin.readline

minute, second = map(int, input().split(':'))

clicked = 0

clicked += minute // 10
clicked += minute % 10

if second >= 30:
    clicked += 1
    clicked += (second - 30) // 10
elif second < 30:
    clicked += 1
    clicked += second // 10

print(clicked)