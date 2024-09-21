import sys
input = sys.stdin.readline

N, k = map(int, input().split())
grades = sorted(list(map(int, input().split())), reverse=True)

print(grades[k - 1])