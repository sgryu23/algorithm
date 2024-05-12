import sys
import heapq
input = sys.stdin.readline

N = int(input())  # N: 백준이가 외치는 정수의 개수
max_heap, min_heap = [], []

for _ in range(N):
    n = int(input())
    # 최대힙이 비어있거나
    # 현재 입력값이 최대힙에서 제일 작은 값보다 작거나 같으면
    if len(max_heap) == 0 or -max_heap[0] >= n:
        heapq.heappush(max_heap, -n)
    else:
        heapq.heappush(min_heap, n)

    # max_heap 요소 개수가 min_heap 요소 개수 + 1보다 많으면
    if len(max_heap) > len(min_heap) + 1:
        # max_heap에서 제일 큰 값을 빼서 min_heap으로 넣어준다.
        number = -heapq.heappop(max_heap)
        heapq.heappush(min_heap, number)

    # min_heap 길이가 max_heap 보다 길면
    elif len(min_heap) > len(max_heap):
        number = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -number)

    print(-max_heap[0])