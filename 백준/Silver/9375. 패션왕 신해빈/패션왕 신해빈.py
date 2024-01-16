import sys
input = sys.stdin.readline

test_case = int(input())
for tc in range(test_case):
    n = int(input())  # n: 의상의 수
    clothes_dict = {}
    for i in range(n):
        clothes = list(input().split())
        if clothes[1] in clothes_dict:
            clothes_dict[clothes[1]].append(clothes[0])
        else:
            clothes_dict[clothes[1]] = [clothes[0]]
    answer = 1

    for j in clothes_dict:
        answer *= (len(clothes_dict[j]) + 1)
    print(answer - 1)