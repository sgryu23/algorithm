import sys
from collections import deque
input = sys.stdin.readline

N = int(input())  # N: 명령의 수
queue = deque()  # 스택으로 사용하면 pop(0) 때문에 시간초과가 남

for _ in range(N):
    command = list(input().split())
    if len(command) >= 2:
        queue.append(int(command[1]))
    elif command[0] == 'pop':
        if queue:
            output = queue.popleft()
            print(output)
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)