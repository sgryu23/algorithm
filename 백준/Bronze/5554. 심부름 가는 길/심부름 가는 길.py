import sys
input = sys.stdin.readline

seconds = 0

for _ in range(4):
    seconds += int(input())

minutes = seconds // 60
print(minutes)

seconds -= minutes * 60
print(seconds)