import sys
input = sys.stdin.readline

N, M = map(int, input().split())
know_truth = [1] * (N + 1)
people = list(map(int, input().split()))
ans = 0

for p in range(1, people[0] + 1):
    know_truth[people[p]] = 0  # 진실을 아는 사람

tmp = []
ans = []

for m in range(M):
    party = list(map(int, input().split()))
    include_know_truth = False
    for i in range(1, party[0] + 1):
        if know_truth[party[i]] == 0:
            include_know_truth = True
            break
    if include_know_truth:
        for person in party[1:]:  # 모두 다 진실을 알게 됨
            know_truth[person] = 0
    else:
        tmp.append(party[1:])  # 임시로 담아줌

check = 0
while check < 2500:  # 리스트 안에 진실을 들은 사람이 없을 때까지 반복
    for tmp_element_list in tmp:
        hear_truth = False
        for element in tmp_element_list:
            if know_truth[element] == 0:
                hear_truth = True
                for k in tmp_element_list:
                    know_truth[k] = 0
                # tmp.remove(tmp_element_list)
                break
    check += 1

for li in tmp:
    is_answer = True
    for e in li:
        if know_truth[e] == 0:
            is_answer = False
            break
    if is_answer:
        ans.append(li)
print(len(ans))