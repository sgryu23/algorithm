import sys
input = sys.stdin.readline


def simulation():
    # is_continue = False
    while True:
        is_continue = False
        for r in range(1, R - 1):
            for c in range(1, C - 1):
                now = rain[r][c]
                for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                    now = min(now, max(origin[nr][nc], rain[nr][nc]))
                if rain[r][c] > now:
                    rain[r][c] = now
                    is_continue = True

        if not is_continue:
            break

    return count()


def count():
    total_rain = 0
    for row_ in range(R):
        for col_ in range(C):
            if rain[row_][col_] > origin[row_][col_]:
                total_rain += rain[row_][col_] - origin[row_][col_]
    return total_rain


T = int(input())  # T: test case
for tc in range(T):
    R, C = map(int, input().split())
    origin = [[0 for _ in range(C)] for _ in range(R)]
    rain = [[0 for _ in range(C)] for _ in range(R)]

    for i in range(R):
        row = list(map(int, input().split()))
        for j in range(C):
            origin[i][j] = row[j]
            if i == 0 or i == R - 1 or j == 0 or j == C - 1:
                rain[i][j] = origin[i][j]
            else:
                rain[i][j] = 1000

    answer = simulation()

    print(f'Case #{tc + 1}: {answer}')