import sys
input = sys.stdin.readline


# 이분 탐색 함수
def binary_search(arr, num):
    left = -1
    right = len(arr)
    while left + 1 < right:
        mid = (left + right) // 2
        if num > arr[mid]:
            left = mid
        else:
            right = mid

    return right


N = int(input())  # N: 수열 A의 크기
sequence = list(map(int, input().split()))  # sequence: 수열
li = [-1000000001]
li_total = [(-1000000001, 0)]  # number, index
sequence = sequence[::-1]

while sequence:
    element = sequence.pop()

    if element > li[-1]:
        li_total.append((element, len(li)))
        li.append(element)
    else:
        idx = binary_search(li, element)
        li[idx] = element
        li_total.append((element, idx))

li_len = len(li) - 1
arr = []

while li_total and li_len:
    val, idx = li_total.pop()
    if idx == li_len:
        arr.append(val)
        li_len -= 1

print(len(arr))
print(' '.join(map(str, arr[::-1])))