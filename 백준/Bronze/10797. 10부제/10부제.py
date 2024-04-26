import sys
input = sys.stdin.readline
day = int(input())
cars = list(map(int, input().split()))
print(cars.count(day))