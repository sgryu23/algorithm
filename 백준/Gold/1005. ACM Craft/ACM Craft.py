import sys
from collections import deque
input = sys.stdin.readline


def bfs(num):
    global destination
    dq = deque([num])
    construction_time[num] = time[num]
    while dq:
        now = dq.popleft()
        if adj_list[now]:
            for adj in adj_list[now]:
                if construction_time[adj] < construction_time[now] + time[adj]:
                    construction_time[adj] = construction_time[now] + time[adj]
                    dq.append(adj)
        else:
            destination.append(now)


t = int(input())
for case in range(t):
    n, k = map(int, input().split())  # n: 건물의 개수, k: 건설순서 규칙
    time = [0] + list(map(int, input().split()))  # time: 건물 건설에 걸리는 시간

    adj_list = [[] for i in range(n + 1)]  # 인접 리스트
    construction_time = [0] * (n + 1)  # 건물 짓는데 걸린 시간을 기록하는 리스트
    for order in range(k):
        a, b = map(int, input().split())
        adj_list[b].append(a)  # 역방향으로 진행
    start = int(input())  # start: 시작점
    destination = []  # 도착 노드 저장 리스트
    bfs(start)
    max_val = 0
    for j in destination:
        if construction_time[j] > max_val:
            max_val = construction_time[j]
    print(max_val)