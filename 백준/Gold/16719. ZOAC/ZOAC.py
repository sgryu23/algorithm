import sys
input = sys.stdin.readline


def string(arr, start):
    if not arr:
        return
    min_val = min(arr)
    idx = arr.index(min_val)
    result[start + idx] = min_val
    print(''.join(result))
    string(arr[idx + 1:], start + idx + 1)
    string(arr[:idx], start)


string_list = list(input().rstrip())
result = [''] * len(string_list)

string(string_list, 0)