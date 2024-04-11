import sys
input = sys.stdin.readline

N = int(input())
S = list(input())

chicken = S.count('C')    # 치킨을 먹는 날
no_chicken = N - chicken  # 치킨을 안 먹는 날

if no_chicken == 0:
    print(N)
else:
    print(N // (no_chicken + 1))