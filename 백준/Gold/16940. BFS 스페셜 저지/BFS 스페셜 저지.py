import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(N + 1)]
visited = [-1] * (N + 1)
children = [set() for _ in range(N + 1)]

for _ in range(N-1):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

specialJudge = list(map(int, input().split()))
res = 1
if specialJudge[0] != 1:
    print(0)
    quit()

visited[1] = True
dq = deque([1])

while dq:
    now = dq.popleft()

    for e in arr[now]:
        if visited[e] == -1:
            visited[e] = visited[now] + 1
            children[now].add(e)
            dq.append(e)

now_idx = 1
for i in specialJudge:
    if now_idx == N:
        break
    child_length = len(children[i])
    child1 = set(specialJudge[now_idx:now_idx + child_length])
    child2 = children[i]
    if child1 != child2:
        res = 0
    now_idx += child_length

print(res)