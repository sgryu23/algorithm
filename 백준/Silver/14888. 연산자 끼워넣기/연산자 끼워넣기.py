import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline


def dfs(depth, now, calculator_index):
    global max_val, min_val
    now_val = now
    if depth == N:
        if now_val > max_val:
            max_val = now_val
        if min_val > now_val:
            min_val = now_val
        return

    if calculator_index == 0:
        now_val += numbers[depth]
    elif calculator_index == 1:
        now_val -= numbers[depth]
    elif calculator_index == 2:
        now_val *= numbers[depth]
    else:
        if now_val >= 0:
            now_val //= numbers[depth]
        else:
            now_val = -(abs(now_val) // numbers[depth])

    if sum(calculators) == 0:
        min_val = min(min_val, now_val)
        max_val = max(max_val, now_val)

    for i in range(4):
        if calculators[i] > 0:
            calculators[i] -= 1
            dfs(depth + 1, now_val, i)
            calculators[i] += 1


N = int(input())
numbers = list(map(int, input().split()))
calculators = list(map(int, input().split()))

max_val = -1000000001
min_val = 1000000001

for k in range(4):
    if calculators[k] > 0:
        calculators[k] -= 1
        dfs(1, numbers[0], k)
        calculators[k] += 1

print(max_val)
print(min_val)