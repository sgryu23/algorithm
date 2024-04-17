import sys
input = sys.stdin.readline

N = int(input())

# N이 한 자리 수인 경우
if N < 10:
    print(N)
elif N < 100:
    print(N)
else:
    answer = 99
    for i in range(100, N + 1):
        hundred = i // 100
        ten = (i - hundred * 100) // 10
        one = i - hundred * 100 - ten * 10
        if hundred - ten == ten - one:
            answer += 1

    print(answer)