import sys
input = sys.stdin.readline

# 문제 정리
# M개의 주사위 -> i 번째 주사위가 N(i)면체 주사위, 모든 면 값의 sum을 S(i)라
# 예시: X == 11, Q == 7 / 3 -> 3 ** (-1) === 4 (mod 11)
# 기약분수 형태: 7 * (3 ** (-1))에서 a == 7, b == 3 ** (-1)
# b ** (X-1) ≡ 1 (mod X) 페르마의 소정리(개념 학습 필요)

# BOJ 1629 곱셈 참고(분할 정복을 통한 거듭제곱)
# def multi(a, b, c):
#     if b == 1:
#         return a % c
#     elif b % 2 == 0:
#         return (multi(a, b//2, c) ** 2) % c
#     else:
#         return((multi(a, b//2, c) ** 2) * a) % c

# 문제 이해가 어려웠던 문제(+페르마의 소정리 개념, 분할 정복을 통한 거듭제곱)


def fermat_s_little_theorem(n, x):
    if x == 1:
        return n
    divide = fermat_s_little_theorem(n, x // 2)
    if x % 2 == 0:
        return divide * divide % MOD
    else:
        return divide * divide * n % MOD


MOD = 1000000007
M = int(input())  # 주사위 개수
ans = 0
for i in range(M):
    N, S = map(int, input().split())  # N: N면체 주사위, S: 해당 주사위의 총합
    calculated_N = fermat_s_little_theorem(N, MOD - 2)
    ans = (ans + calculated_N * S % MOD) % MOD

print(ans)