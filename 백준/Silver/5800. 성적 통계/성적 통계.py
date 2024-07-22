import sys
input = sys.stdin.readline

K = int(input())

for i in range(1, K + 1):
    print(f'Class {i}')
    data = list(map(int, input().split()))
    grades = sorted(data[1:], reverse=True)
    max_ = max(grades)
    min_ = min(grades)
    largest_gap = 0
    for j in range(len(grades) - 1):
        if abs(grades[j + 1] - grades[j]) > largest_gap:
            largest_gap = abs(grades[j + 1] - grades[j])
    print(f'Max {max_}, Min {min_}, Largest gap {largest_gap}')