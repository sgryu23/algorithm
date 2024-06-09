import sys
from itertools import combinations as c
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = sum(cards)
sum_combinations = set()

for i in range(1, N + 1):
    for j in c(cards, i):
        sum_combinations.add(sum(j))

print(M - len(sum_combinations))