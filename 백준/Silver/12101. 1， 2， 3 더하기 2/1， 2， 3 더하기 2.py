import sys
input = sys.stdin.readline


def sum_(number_list):
    if sum(number_list) == n:
        temp = []
        for a in number_list:
            temp.append(a)
        answer_list.append(temp)
        return
    elif sum(number_list) > n:
        return
    else:
        for num in one_two_three:
            number_list.append(num)
            sum_(number_list)
            number_list.pop()


n, k = map(int, input().split())
one_two_three = [1, 2, 3]
answer_list = []
sum_([])
if k > len(answer_list):
    print(-1)
else:
    answer = ''
    for i in answer_list[k - 1][:-1]:
        answer += (str(i) + '+')
    answer += str(answer_list[k - 1][-1])

    print(answer)