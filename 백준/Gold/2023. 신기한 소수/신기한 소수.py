import sys


def is_prime_number(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def solve(number):
    if len(str(number)) == N:
        if is_prime_number(number):
            print(number)
        return

    for j in range(10):
        k = number * 10 + j
        if is_prime_number(k):
            solve(k)


N = int(sys.stdin.readline().rstrip())

for i in [2, 3, 5, 7]:
    solve(i)