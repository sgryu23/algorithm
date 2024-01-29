import sys
input = sys.stdin.readline

t = int(input())  # t: 테스트 케이스 개수
P_N = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0] * 90
for element in range(11, 101):
    P_N[element] = P_N[element - 1] + P_N[element - 5]

for tc in range(t):
    print(P_N[int(input())])