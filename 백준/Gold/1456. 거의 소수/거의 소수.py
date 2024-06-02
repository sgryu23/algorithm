import sys

M, N = map(int, sys.stdin.readline().split())

is_prime_number_list = [1 for i in range(int(N ** 0.5) + 1)]
is_prime_number_list[1] = 0

for j in range(2, int(N ** 0.5) + 1):
    if is_prime_number_list[j]:
        if j * j > int(N ** 0.5):
            break
        for k in range(j ** 2, int(N ** 0.5) + 1, j):
            is_prime_number_list[k] = 0

answer = 0
for l in range(1, len(is_prime_number_list)):
    if is_prime_number_list[l]:
        number = l * l
        while True:
            if number < M:
                number *= l
                continue
            if number > N:
                break
            number *= l
            answer += 1

print(answer)