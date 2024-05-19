import sys
n = int(sys.stdin.readline())

fibonacci = [0 for _ in range(n + 1)]

if n <= 1:
    if n == 0:
        print(0)
    else:
        print(1)
else:
    fibonacci[1] = 1
    fibonacci[2] = 1
    for i in range(3, n + 1):
        fibonacci[i] = fibonacci[i - 2] + fibonacci[i - 1]
    print(fibonacci[n])