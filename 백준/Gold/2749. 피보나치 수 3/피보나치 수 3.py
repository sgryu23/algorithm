import sys
input = sys.stdin.readline

fibonacci = [0, 1]

n = int(input())
mod = 10 ** 6
pisano_period = mod // 10 * 15

for i in range(2, pisano_period):
    fibonacci.append((fibonacci[i - 1] + fibonacci[i - 2]) % mod)
    
print(fibonacci[n % pisano_period])