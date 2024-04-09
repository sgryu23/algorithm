import sys
input = sys.stdin.readline

N = int(input())
P = int(input())

if N < 5:
    answer = P
elif 5 <= N < 10:
    answer = P - 500
elif 10 <= N < 15:
    answer = min(P - 500, P * 9 // 10)
elif 15 <= N < 20:
    answer = min(P - 500, P * 9 // 10, P - 2000)
else:
    answer = min(P - 500, P * 9 // 10, P - 2000, P * 75 // 100)

if answer < 0:
    print(0)
else:
    print(answer)