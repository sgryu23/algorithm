import sys
input = sys.stdin.readline

x = int(input())

target = 1

while x > target:
    x -= target
    target += 1

if target % 2 == 0:
    son = x
    mother = target - x + 1
else:
    son = target - x + 1
    mother = x

print(son, '/', mother, sep='')