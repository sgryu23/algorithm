import sys
input = sys.stdin.readline

n = int(input())
if n == 0:
    print(1)
else:
    new_number = (n % 10) * 10 + (n // 10 + n % 10) % 10
    cycle = 1
    while n != new_number:
        new_number = (new_number % 10) * 10 + (new_number // 10 + new_number % 10) % 10
        cycle += 1
    print(cycle)