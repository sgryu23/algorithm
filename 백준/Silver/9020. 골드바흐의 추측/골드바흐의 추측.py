import sys
input = sys.stdin.readline


def is_prime_number(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


T = int(input())
for _ in range(T):
    N = int(input())

    left, right = N // 2, N // 2
    while left > 0:
        if is_prime_number(left) and is_prime_number(right):
            print(left, right)
            break
        else:
            left -= 1
            right += 1