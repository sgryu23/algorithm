import sys
input = sys.stdin.readline

x, y = map(int, input().split())
days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
accumulated_days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
answer = (accumulated_days[x - 1] + y) % 7 - 1
print(days[answer])