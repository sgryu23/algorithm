import sys
input = sys.stdin.readline


def permutation(str_list):
    global order, find_answer
    if order == number and not find_answer and len(str_list) == len(string_list):
        answer = ''
        for a in str_list:
            answer += a
        find_answer = True
        print(f'{string} {number} = {answer}')
        return

    if len(str_list) == len(string_list):
        order += 1
        return

    for i in range(len(string_list)):
        if visited[i] == 0:
            str_list.append(string_list[i])
            visited[i] = 1
            permutation(str_list)
            str_list.pop()
            visited[i] = 0


while True:
    try:
        string, number = input().split()
        string_list = list(string)
        number = int(number)
        num = len(string_list)
        is_permutation = 1
        while num > 1:
            is_permutation *= num
            num -= 1

        if number > is_permutation:
            print(f'{string} {number} = No permutation')
        else:
            order = 1
            find_answer = False
            visited = [0 for _ in range(len(string_list))]
            permutation([])

    except:
        break
