import sys

while True:
    input_ = sys.stdin.readline().rstrip()

    if input_ == '#':
        break

    if input_[-1] == 'e':
        answer = ''
        number = 0
        for i in input_:
            if i == 'e':
                if number % 2 == 0:
                    answer += '0'
                else:
                    answer += '1'
            else:
                if int(i):
                    answer += i
                    number += 1
                else:
                    answer += i
    else:
        answer = ''
        number = 0
        for i in input_:
            if i == 'o':
                if number % 2 == 1:
                    answer += '0'
                else:
                    answer += '1'
            else:
                if int(i):
                    answer += i
                    number += 1
                else:
                    answer += i

    print(answer)