import sys
from collections import deque
input = sys.stdin.readline

while True:
    L, R, C = map(int, input().split())  # L: L 번 주어짐, R: 행, C: 열
    if L == R == C == 0:
        break

    arr = [[] for _ in range(L)]
    visited = [[[0 for cc in range(C)] for rr in range(R)] for ll in range(L)]
    S_L, S_R, S_C = 0, 0, 0

    for l in range(L):
        for r in range(R):
            input_list = list(input().rstrip())
            if 'S' in input_list:
                S_C = input_list.index('S')
                S_R, S_L = r, l
            arr[l].append(input_list)
        blank = input()

    dq = deque()
    dq.append((S_L, S_R, S_C))
    minimum_minute = 0
    escaped = False

    while dq and not escaped:
        minimum_minute += 1

        for j in range(len(dq)):
            lv, row, col = dq.popleft()
            for nl, nr, nc in [[lv + 1, row, col], [lv - 1, row, col], [lv, row + 1, col], [lv, row - 1, col], [lv, row, col + 1], [lv, row, col - 1]]:
                if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C:
                    if arr[nl][nr][nc] == 'E':
                        escaped = True
                        break
                    if visited[nl][nr][nc] == 0 and arr[nl][nr][nc] == '.':
                        visited[nl][nr][nc] = 1
                        dq.append((nl, nr, nc))

    if escaped:
        print(f'Escaped in {minimum_minute} minute(s).')
    else:
        print('Trapped!')