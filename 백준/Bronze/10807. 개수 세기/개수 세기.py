import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
v = int(input())
print(lst.count(v))