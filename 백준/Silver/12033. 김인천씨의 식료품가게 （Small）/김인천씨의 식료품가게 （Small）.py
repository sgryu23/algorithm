import sys
from collections import deque
input = sys.stdin.readline

T = int(input())  # T: 테스트 케이스 개수

for test_case in range(1, T + 1):
    N = int(input())  # N: 상품수
    dq = deque()
    dummy = list(map(int, input().split()))
    answer = []
    for price in dummy:
        if price * 3 // 4 in dq:
            answer.append(dq[0])
            dq.popleft()
        else:
            dq.append(price)
    print(f'Case #{test_case}:', *answer)