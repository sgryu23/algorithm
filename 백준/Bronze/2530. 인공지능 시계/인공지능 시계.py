import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
seconds = int(input())

hour = seconds // 3600
A += hour
seconds -= 3600 * hour

minute = seconds // 60
B += minute
seconds -= 60 * minute

C += seconds

if C >= 60:
    B += 1
    C -= 60

if B >= 60:
    A += 1
    B -= 60

if A >= 24:
    A -= 24 * (A // 24)

print(A, B, C)