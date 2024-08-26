import sys, math


def is_palindrome(number):
    if str(number) == str(number)[::-1]:
        return True
    return False


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


N = int(sys.stdin.readline())

while True:
    if is_prime(N) and is_palindrome(N):
        print(N)
        break
    N += 1