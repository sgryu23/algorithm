import sys
input = sys.stdin.readline

n, s = map(int, input().split())  # n: 수열의 길이, s: 부분합 중 s 이상인 것
numbers = list(map(int, input().split()))

left, right = 0, 0
sum_ = 0
min_len = n + 1

while True:
    if sum_ >= s:
        min_len = min(min_len, right - left)
        sum_ -= numbers[left]
        left += 1
    elif right == n:
        break
    else:
        sum_ += numbers[right]
        right += 1

if min_len == n + 1:
    print(0)
else:
    print(min_len)