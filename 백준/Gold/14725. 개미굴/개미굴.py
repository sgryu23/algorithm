import sys
input = sys.stdin.readline

# 아이디어 정리
# 정렬 후 겹치는 부분까지 인덱스로 접근 후 print

N = int(input())  # N: 먹이의 정보 개수
trees = []
dash = '--'
for _ in range(N):
    info = list(input().split())
    trees.append(info[1:])  # 첫 부분의 숫자는 어떻게 활용할지 몰라서 버림

trees.sort()  # 문자열 순서대로 정렬

for i in range(len(trees)):
    if i == 0:  # 첫 번째 리스트 값은 그대로 출력
        for j in range(len(trees[i])):
            print(dash * j + trees[i][j])
    else:
        idx = 0
        for k in range(len(trees[i])):
            # 이전 리스트 원소와 겹치는 것이 없을 경우
            if trees[i - 1][k] != trees[i][k] or len(trees[i - 1]) <= k:
                break
            # 겹치는 원소가 존재하면 idx 조정
            else:
                idx = k + 1
        for l in range(idx, len(trees[i])):
            print(dash * l + trees[i][l])