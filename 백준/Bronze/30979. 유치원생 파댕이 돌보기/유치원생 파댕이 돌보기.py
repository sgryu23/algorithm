import sys
input = sys.stdin.readline

T = int(input())
N = int(input())
if sum(list(map(int, input().split()))) >= T:
    print('Padaeng_i Happy')
else:
    print('Padaeng_i Cry')