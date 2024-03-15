import sys
input = sys.stdin.readline

n = int(input())  # n: 사진틀의 개수
total = int(input())  # total: 전체 학생의 총 추천 횟수
get_recommend = list(map(int, input().split()))

final_cand = []
student_num = [0 for _ in range(101)]

for i in get_recommend:
    if len(final_cand) == n and i not in final_cand:
        min_get_recommend = 1001
        min_get_recommend_index = 0
        for j in range(n - 1, -1, -1):
            if min_get_recommend >= student_num[final_cand[j]]:
                min_get_recommend = student_num[final_cand[j]]
                min_get_recommend_index = j

        student_num[final_cand[min_get_recommend_index]] = 0
        final_cand.remove(final_cand[min_get_recommend_index])

        student_num[i] += 1
        final_cand.append(i)
    else:
        student_num[i] += 1
        if i not in final_cand:
            final_cand.append(i)

final_cand.sort()
for k in final_cand:
    print(k, end=' ')