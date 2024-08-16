import sys
input = sys.stdin.readline

N = int(input())
cards = {}

for _ in range(N):
    card = int(input())
    if card in cards:
        cards[card] += 1
    else:
        cards[card] = 1

answer = sorted(cards.items(), key= lambda x : (-x[1], x[0]))
print(answer[0][0])