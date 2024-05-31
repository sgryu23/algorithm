import sys
input = sys.stdin.readline


def prime_number(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        last = round(number ** 0.5) + 1
        for i in range(3, last, 2):
            if number % i == 0:
                return False
    return True


while True:
    x = int(input())
    if x == 0:
        break
    answer = 0
    for j in range(x + 1, x * 2 + 1):
        if prime_number(j):
            answer += 1
    print(answer)