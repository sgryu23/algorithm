import sys
input = sys.stdin.readline

n, w, L = map(int, input().split())  # n: 트럭의 수, w: 다리의 길이, L: 최대 하중
trucks = list(map(int, input().split()))
bridge = [0] * w

answer = 0

# 모든 트럭이 지나갈 때까지 반복
while bridge:
    answer += 1
    bridge.pop(0)
    if trucks:
        if sum(bridge) + trucks[0] <= L:
            bridge.append(trucks.pop(0))
        else:
            bridge.append(0)

print(answer)