import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # N: 바구니 수, M: 뒤집을 횟수
baskets = [a for a in range(N + 1)]
for _ in range(M):
    i, j = map(int, input().split())
    temp_baskets = [0 for k in range(N + 1)]
    for l in range(j, i - 1, -1):
        temp_baskets[i + j - l] = baskets[l]
    for b in range(1, N + 1):
        if temp_baskets[b] == 0:
            temp_baskets[b] = baskets[b]
    baskets = temp_baskets

baskets = baskets[1:]
print(*baskets)