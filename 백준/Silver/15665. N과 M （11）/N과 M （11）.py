import sys
input = sys.stdin.readline


def n_and_m(lst):
    if len(lst) == M:
        print(*lst)
        return

    for i in range(len(subsequence)):
        lst.append(subsequence[i])
        n_and_m(lst)
        lst.pop()


N, M = map(int, input().split())
subsequence = sorted(list(set(map(int, input().split()))))
li = []

for j in range(len(subsequence)):
    li.append(subsequence[j])
    n_and_m(li)
    li.pop()