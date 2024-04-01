import sys
input = sys.stdin.readline

N, B = map(int, input().split())  # N: N개의 물건, B: 시흠이의 돈
cand = []
coupon_cand = []

for i in range(N):
    p, s = map(int, input().split())  # p: 가격, s: 배송비
    cand.append([p + s, p // 2 + s])

cand.sort(key=lambda x: x[0])

answer = 0

for i in range(N):
    temp_answer = 0
    temp_money = B
    if temp_money - cand[i][1] >= 0:
        temp_answer += 1
        temp_money -= cand[i][1]
    else:
        continue
    for j in range(N):
        if i != j:
            if temp_money - cand[j][0] >= 0:
                temp_answer += 1
                temp_money -= cand[j][0]
            else:
                break
    answer = max(answer, temp_answer)
print(answer)