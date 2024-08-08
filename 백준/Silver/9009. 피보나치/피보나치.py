import sys
input = sys.stdin.readline

T = int(input())

fibonacci = [0 for _ in range(50)]
fibonacci[1] = 1

for i in range(2, 50):
    fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]

for _ in range(T):
    n = int(input())
    arr = []

    while n:
        for j in range(50):
            if fibonacci[j] <= n:
                temp = fibonacci[j]

        n -= temp
        arr.append(temp)
        arr.sort()

    for k in arr:
        print(k, end=' ')
    print()