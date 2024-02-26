import sys
input = sys.stdin.readline

n = int(input())
_list = []
for i in range(n):
    m = int(input())
    _list.append(m)
_list.sort()
for e in _list:
    print(e)