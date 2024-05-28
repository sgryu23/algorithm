import sys
from collections import deque


def pour(x, y):
    if visited[x][y] == 0:
        visited[x][y] = 1
        queue.append((x, y))


def solution():
    while queue:
        # A 물통의 물: a_water, B 물통의 물: b_water, C 물통의 물: c_water 라 하자.
        a_water, b_water = queue.popleft()
        c_water = C - a_water - b_water

        # A 물통이 비어있는 경우에 C 물통에 남아있는 양 저장
        if a_water == 0:
            answer.append(c_water)

        # A -> B 로 물 이동
        water = min(a_water, B - b_water)
        pour(a_water - water, b_water + water)

        # A -> C 로 물 이동
        water = min(a_water, C - c_water)
        pour(a_water - water, b_water)

        # B -> C 로 물 이동
        water = min(b_water, C - c_water)
        pour(a_water, b_water - water)

        # B -> A 로 물 이동
        water = min(b_water, A - a_water)
        pour(a_water + water, b_water - water)

        # C -> A 로 물 이동
        water = min(c_water, A - a_water)
        pour(a_water + water, b_water)

        # C -> B로 물 이동
        water = min(c_water, B - b_water)
        pour(a_water, b_water + water)


A, B, C = map(int, sys.stdin.readline().split())

answer = []
queue = deque()
visited = [[0 for c in range(B + 1)] for r in range(A + 1)]
visited[0][0] = 1
queue.append((0, 0))

solution()

answer.sort()

for ans in answer:
    print(ans, end=" ")