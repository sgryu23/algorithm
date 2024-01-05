import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())  # N: 보석, K: 가방 개수
queue = []
bags = []
ans = 0

for n in range(N):
    M, V = map(int, input().split())  # M: 무게, V: 가격 (M 순서대로 우선정렬)
    heapq.heappush(queue, [M, V])

for k in range(K):
    C = int(input())
    bags.append(C)

bags.sort()   # 시간 초과 때문에 bags 정렬을 안 해줬는데 방법이 없는 것 같아서 일단 시도

tmp = []
for bag in bags:
    while queue and bag >= queue[0][0]:
        heapq.heappush(tmp, -heapq.heappop(queue)[1])
    if tmp:
        ans -= heapq.heappop(tmp)
    elif not queue:   # else 로 했는데 queue가 없을 때로 해야 했음
        break

print(ans)