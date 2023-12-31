def multi(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return (multi(a, b//2, c) ** 2) % c
    else:
        return((multi(a, b//2, c) ** 2) * a) % c


v1, v2, v3 = map(int, input().split())
print(multi(v1, v2, v3))