import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())  # N: 세로, M: 가로, K: 관중석 번호
n = K // M
m = K - n * M
print(n, m)