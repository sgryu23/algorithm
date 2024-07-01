import sys
input = sys.stdin.readline

N = int(input())

li = [tuple(map(int, input().rstrip().split())) for _ in range(N)]
li.sort(key=lambda x: x[1])
time, end = li.pop()
end -= time

while li:
    t, e = li.pop()
    if e > end:
        end -= t
    else:
        end = e
        end -= t
    if end < 0:
        print(-1)
        quit()

print(end)