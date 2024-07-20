import sys
input = sys.stdin.readline


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


a, b = map(int, input().split())
c, d = map(int, input().split())

numerator = b * c + a * d
denominator = b * d

num = gcd(numerator, denominator)

numerator = int(numerator / num)
denominator = int(denominator / num)

print(numerator, denominator)