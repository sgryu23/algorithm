import sys
input = sys.stdin.readline


def find_min(dot):
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2

        if dots[mid] < dot:
            start = mid + 1
        else:
            end = mid - 1

    return end + 1


def find_max(dot):
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2

        if dot < dots[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return end


N, M = map(int, input().split())
dots = sorted(list(map(int, input().split())))

for _ in range(M):
    start, end = map(int, input().split())
    print(find_max(end) - find_min(start) + 1)