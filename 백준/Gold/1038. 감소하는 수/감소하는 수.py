import sys
from itertools import combinations

N = int(sys.stdin.readline().rstrip())

result = []
for i in range(1, 11):
    for j in combinations(range(10), i):
        number = ''.join(list(map(str, reversed(list(j)))))
        result.append(int(number))

result.sort()

if N >= len(result):
    print(-1)
else:
    print(result[N])