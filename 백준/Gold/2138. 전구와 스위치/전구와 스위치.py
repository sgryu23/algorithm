import sys
import copy
input = sys.stdin.readline


def switch(state1, state2):
    state1_copy = copy.deepcopy(state1)
    change = 0
    for i in range(1, n):
        if state1_copy[i - 1] == state2[i - 1]:
            continue
        # 목표 상태와 다르면 스위치를 1회 눌러주고 i - 1 ~ i + 1 위치의 상태를 바꿔준다.
        change += 1
        for j in range(i - 1, i + 2):
            if j < n:
                state1_copy[j] = 1 - state1_copy[j]  # 상태 변경

    if state1_copy == state2:
        return change
    else:
        return 1e9


n = int(input())  # n: 전구, 스위치 개수
bulbs = list(map(int, input().rstrip()))
target = list(map(int, input().rstrip()))

answer = switch(bulbs, target)

# 첫 번째 스위치를 누르는 경우
bulbs[0] = 1 - bulbs[0]
bulbs[1] = 1 - bulbs[1]

# 첫 번째 전구를 안 켠 경우 & 첫 번째 전구를 켠 경우 비교해서 낮은 값 출력
answer = min(answer, switch(bulbs, target) + 1)
if answer != 1e9:
    print(answer)
else:
    print(-1)