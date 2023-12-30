import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)  # recursion error 방지용

# 아이디어 정리
# cycle 을 어떻게 판별할 것인지가 관건
# 시간 초과도 생각해야 함(가지치기)
# 인덱스 슬라이싱을 어떻게 해줘야 할지 고민하는 데 시간을 많이 씀
# 풀고 나면 막상 복잡한 문제는 아니었는데 생각 접근 방법을 떠올리는 게 어려웠던 문제


def dfs(num):
    global ans

    visited[num] = True
    cycle.append(num)

    if visited[students[num]]:  # 다음으로 갈 곳을 이미 방문 했으면(가지치기)
        if students[num] in cycle:  # 이미 갔던 곳이라면
            # 인덱스 슬라이싱이 핵심
            ans -= len(cycle[cycle.index(students[num]):])
        return
    else:
        dfs(students[num])  # 다음 방문할 곳으로 방문


T = int(input().rstrip())  # T: 테스트 케이스의 개수
for tc in range(T):
    n = int(input())  # n: 학생의 수
    students = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    ans = n
    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []  # 돌 때마다 cycle을 만들어서 돌아오는지 구분해줘야 했음
            dfs(i)

    print(ans)