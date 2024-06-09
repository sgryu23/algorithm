import sys
input = sys.stdin.readline

N = int(input())  # N: 마트료시카 개수
sizes = sorted(list(map(int, input().split())))

answer = N

if N == 1:
    print(1)
else:
    visited = [0 for _ in range(N)]
    while True:
        able_to_loop = False
        for i in range(N):
            if visited[i] == 0:
                now = sizes[i]
                visited[i] = 1
                able_to_loop = True
                break
        if able_to_loop:
            for size in range(1, N):
                if sizes[size] > now and visited[size] == 0:
                    answer -= 1
                    now = sizes[size]
                    visited[size] = 1
        else:
            break

    print(answer)