import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().rstrip().split()))
cards_set = set(cards)
max_val = max(cards)
score = [0 for _ in range(max_val + 1)]

for i in cards:
    if i == max_val:
        continue
    for j in range(2 * i, max_val + 1, i):
        if j in cards_set:
            score[i] += 1
            score[j] -= 1

for l in cards:
    print(score[l], end=' ')