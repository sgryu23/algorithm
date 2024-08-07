import sys
input = sys.stdin.readline


def func():
    if len(li) == n:
        print(*li)
        return
    for i in range(1, n + 1):
        if i not in li:
            li.append(i)
            func()
            li.pop()


n = int(input())
li = []

func()