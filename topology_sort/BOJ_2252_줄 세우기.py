# 아이디어 정리
# 위상 정렬 문제

import sys
from collections import deque

input = sys.stdin.readline

# 0. 준비: 입력값 받고 간선 연결 리스트 세팅
N, M = map(int, input().split())     # N: 사람의 수(노드의 개수), M: 순서 쌍의 수(간선 개수)
students = [0] * (N + 1)             # students: 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트
graph = [[] for _ in range(N + 1)]   # 각 사람에 연결된 간선 정보를 담기 위한 연결 리스트

for _ in range(M):
    front, back = map(int, input().split())
    graph[front].append(back)
    students[back] += 1

# 1. 위상 정렬 함수
def topology_sort():
    result = []
    dq = deque()

    for i in range(1, N + 1):
        if students[i] == 0:
            dq.append(i)

    while dq:
        now = dq.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드의 진입차수에서 1씩 빼기
        for j in graph[now]:
            students[j] -= 1
            if students[j] == 0:
                dq.append(j)

    # 위상 정렬 수행한 결과 출력
    for res in result:
        print(res, end=' ')

# 2. 함수 실행 및 값 출력
topology_sort()

# 시간 복잡도는 O(V+E)
# 위상 정렬을 수행할 때 차례대로 모든 노드를 확인하면서(O(V)), 해당 노드에서 출발하는 간선을 차례대로 제거(O(E))해야 한다.
# 따라서 노드와 간선을 모두 확인하는 것을 고려해서 O(V) + O(E) = O(V+E)