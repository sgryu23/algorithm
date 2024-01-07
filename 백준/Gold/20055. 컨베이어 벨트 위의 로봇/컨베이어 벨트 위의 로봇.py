import sys
input = sys.stdin.readline

N, K = map(int, input().split())  # N: 벨트의 칸 수, K: 내구도가 0인 칸의 개수가 K개 이상이면 종료
A = list(map(int, input().split()))  # A: 벨트의 내구도
robots = [False for _ in range(N)]
stage = 1
# 0의 개수가 K보다 작을 때 계속 반복
while A.count(0) < K:
    # 1. 벨트가 한 칸 돌아간다.
    tmp = A[-1]
    for i in range(2 * N - 1, 0, -1):
        A[i] = A[i - 1]
        if i < N and robots[i - 1] and not robots[i]:
            robots[i] = True
            robots[i - 1] = False
    A[0] = tmp
    if robots[N - 1]:
        robots[N - 1] = False
    # 2. 로봇 이동하기
    for j in range(N - 1, 0, -1):
        if robots[j - 1] and not robots[j] and A[j] > 0:
            robots[j] = True
            robots[j - 1] = False
            A[j] -= 1
    if robots[N - 1]:  # 내리는 곳에 도착했으면 내려주기
        robots[N - 1] = False
    # print('로봇이 컨베이어 벨트 위에 이동하고 난 뒤에 결과')
    # print(A)
    # print(robots)

    # 3. 로봇을 올릴 수 있으면 올리기
    if A[0] > 0:
        robots[0] = True
        A[0] -= 1
    # print('로봇을 컨베이어 벨트에 새로 올린 결과')
    # print(A)
    # print(robots)
    # print(f'{stage}번째 싸이클')
    # 4. 내구도가 0인 벨트가 K개 이상일 경우 종료
    if A.count(0) >= K:
        break
    stage += 1

print(stage)