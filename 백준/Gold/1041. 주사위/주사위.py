import sys
input = sys.stdin.readline

# 아이디어 정리
# 윗 부분의 꼭짓점은 세 면이 보임: 인접한 세 면 합의 최솟값
# 인접한 세면: min(ABC, ABD, ACE, ADE, BCF, BDF, CEF, DEF) (+는 생략)
# 두 면이 보이는 경우: 테두리
# 인접한 두면 합의 최솟값: min(AB, AC, AD, AE, BC, BD, BF, CE, CF, DE, DF, EF)
# 한 면의 최솟값: min(A, B, C, D, E, F)
# 반례 모음: https://www.acmicpc.net/board/view/121997

N = int(input())
A, B, C, D, E, F = map(int, input().split())
ans = 0
if N > 1:
    # 윗부분 네 꼭짓점의 합
    three_area = min(A+B+C, A+B+D, A+C+E, A+D+E, B+C+F, B+D+F, C+E+F, D+E+F)
    # 세 면의 최소 합이 한 면의 최소합 * 3과 값이 같다면,
    ans += three_area * 4
    two_area = min(A+B, A+C, A+D, A+E, B+C, B+D, C+E, D+E, B+F, C+F, D+F, E+F)
    ans += two_area * (2 * N - 3) * 4
    one_area = min(A, B, C, D, E, F)
    ans += one_area * (N - 2) * (5 * N - 6)
else:
    ans = A+B+C+D+E+F - max(A, B, C, D, E, F)

print(ans)