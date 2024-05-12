import sys
input = sys.stdin.readline


def n_and_m(li, idx):
    if len(li) == M:
        if tuple(li) not in answer_candidate:
            answer_candidate.add(tuple(li))
            for e in li:
                print(e, end=' ')
            print()
        return

    for i in range(idx + 1, N):
        li.append(numbers[i])
        n_and_m(li, i)
        li.pop()


N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
answer_candidate = set()

subsequence = []
for j in range(N):
    if numbers[j] not in subsequence:
        subsequence.append(numbers[j])
        n_and_m(subsequence, j)
        subsequence.pop()