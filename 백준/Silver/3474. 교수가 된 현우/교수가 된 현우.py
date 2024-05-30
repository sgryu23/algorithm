import sys
input = sys.stdin.readline

T = int(input())  # T: 테스트 케이스 개수
for _ in range(T):
    N = int(input())  # N: 정수 N
    # 5의 배수가 멧개고? (2의 배수는 최소 5의 배수보다 많을 수밖에 없음)
    answer = 0
    five_power = 13
    while five_power > 0:
        if N // (5 ** five_power) == 0:
            five_power -= 1
        else:
            answer += N // (5 ** five_power)
            five_power -= 1

    print(answer)