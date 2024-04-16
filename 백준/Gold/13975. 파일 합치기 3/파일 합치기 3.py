import sys
from heapq import heapify, heappush, heappop
input = sys.stdin.readline

T = int(input())  # T: 테스트 케이스
for tc in range(T):
    K = int(input())  # K: 소설 장의 수
    files = list(map(int, input().split()))
    heapify(files)
    cost = 0
    while len(files) > 1:
        file_1 = heappop(files)
        file_2 = heappop(files)
        temp_file = file_1 + file_2
        cost += temp_file
        heappush(files, temp_file)
    print(cost)