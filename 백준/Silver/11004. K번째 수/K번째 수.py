import sys
input = sys.stdin.readline

N, K = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

print(numbers[K - 1])