import sys
input = sys.stdin.readline

N, C = map(int, input().split())  # N: 집의 개수, C: 공유기의 개수
houses = []
for _ in range(N):
    house = int(input())
    houses.append(house)

houses.sort()

smallest = 0   # smallest: 공유기 거리 최소
largest = houses[-1] - houses[0]  # largest: 공유기 거리 최대
result = 0

while smallest <= largest:
    mid = (smallest + largest) // 2
    current = houses[0]
    count = 1

    # 공유기 설치를 몇 대 할 수 있을지 체크
    for i in range(1, len(houses)):
        if houses[i] >= current + mid:
            count += 1
            current = houses[i]

    # 공유기 설치 수가 목표보다 크면 공유기 사이 거리 늘림
    if count >= C:
        smallest = mid + 1
        result = mid
    # 공유기 설치 수가 목표보다 작으면 공유기 사이 거리 줄임
    else:
        largest = mid - 1

print(result)