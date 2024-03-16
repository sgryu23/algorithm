import sys
input = sys.stdin.readline


def gcd(x, y):
    while y:
        if x > y:
            x, y = y, x
        y %= x
    return x


T = int(input())  # T: 테스트 케이스 개수
for tc in range(T):
    a, b = map(int, input().split())
    gcd_number = gcd(a, b)
    print(a * b // gcd_number, gcd_number)