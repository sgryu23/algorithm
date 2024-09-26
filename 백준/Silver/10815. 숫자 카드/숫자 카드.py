import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
figure_out = list(map(int, input().split()))

_dict = {}

for i in range(N):
    _dict[cards[i]] = 0

for j in range(M):
    if figure_out[j] not in _dict:
        print(0, end=' ')
    else:
        print(1, end=' ')