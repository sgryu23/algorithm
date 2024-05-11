import sys
input = sys.stdin.readline


def calc(a, b):
    if b < 0:
        return 0

    result = 1
    current = a

    while b:
        if b & 1:
            result = result * current % mod
        current = current * current % mod
        b //= 2

    return result


N = int(input())  # N: 항의 개수
mod = 1000000007
answer = 0

for _ in range(N):
    C, K = map(int, input().split())
    answer += C * K * calc(2, K - 1)

print(answer % mod)