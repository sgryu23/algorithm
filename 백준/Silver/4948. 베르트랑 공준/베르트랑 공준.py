import sys
input = sys.stdin.readline

while True:
    x = int(input())
    if x == 0:
        break

    is_prime_number = [0] * 2 + [1] * 123456 * 2

    # 에라토스테네스의 체 방법
    for i in range(2, 123456 * 2 + 1):
        # 소수가 아닌 것들은 지워준다.
        if is_prime_number[i]:
            for j in range(i * 2, 123456 * 2 + 1, i):
                is_prime_number[j] = 0

    answer = sum(is_prime_number[x + 1: x * 2 + 1])
    print(answer)