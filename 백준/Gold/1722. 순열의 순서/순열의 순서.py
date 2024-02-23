import sys
input = sys.stdin.readline


def permutation(num):
    if num <= 1:
        return 1
    return num * permutation(num - 1)


n = int(input())
lst = list(map(int, input().split()))

if lst[0] == 1:
    k = lst[1]
    arr = list(range(1, n + 1))
    answer = []

    for i in range(n, 0, -1):
        dividend = permutation(i - 1)
        idx = (k - 1) // dividend
        answer.append(arr[idx])
        arr.remove(arr[idx])
        k -= dividend * idx

    print(*answer)
else:
    combination = lst[1:]
    number_set = list(range(1, n + 1))
    k = 1

    for j in range(n, 0, -1):
        num = permutation(j - 1)
        idx = number_set.index(combination[n - j])
        number_set.remove(number_set[idx])
        k += num * idx

    print(k)