import sys, math
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())  # N: 자연수
if N == 1:
    print(0)
    quit()

max_number = 4000000
answer = 0  # answer: 연속된 소수의 합으로 나타낼 수 있는 경우의 수

is_prime_number = [1 for _ in range(N + 1)]
is_prime_number[0], is_prime_number[1] = 0, 0

for i in range(2, int(math.sqrt(N)) + 1):
    if is_prime_number[i]:
        for j in range(2, N // i + 1):
            is_prime_number[i * j] = 0  # 소수의 배수는 소수가 아니므로 0으로 만듦

prime_numbers = []  # 소수(prime number)만 담아주는 리스트
for k in range(2, N + 1):
    if is_prime_number[k]:
        prime_numbers.append(k)

left, right = len(prime_numbers) - 1, len(prime_numbers) - 1
current = prime_numbers[-1]

# 이분탐색으로 연속된 소수의 합으로 나타낼 수 있는지 판정
while 0 <= left <= right and 0 <= right < len(prime_numbers):
    if current > N:
        current -= prime_numbers[right]
        right -= 1

    else:
        if current == N:
            answer += 1
        left -= 1
        if left < 0:
            break
        current += prime_numbers[left]

print(answer)