import sys
input = sys.stdin.readline


def is_increasing_subsequence(li, index):
    if len(li) == M:
        print(*li)
        return

    for idx in range(index + 1, N):
        li.append(sequence[idx])
        is_increasing_subsequence(li, idx)
        li.pop()


N, M = map(int, input().split())
sequence = sorted(list(map(int, input().split())))
subsequence = []

for i in range(N):
    subsequence.append(sequence[i])
    is_increasing_subsequence(subsequence, i)
    subsequence.pop()