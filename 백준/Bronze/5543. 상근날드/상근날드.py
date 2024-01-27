import sys
input = sys.stdin.readline

burgers = []
drinks = []
for burger in range(3):
    b = int(input())
    burgers.append(b)
for drink in range(2):
    d = int(input())
    drinks.append(d)
print(min(burgers) + min(drinks) - 50)