import sys
input = sys.stdin.readline


def sub_a(string):
    if string == S:
        print(1)
        quit()

    if len(string) > len(S) and string[-1] == 'A':
        result_string = string[:-1]
        sub_a(result_string)
        sub_b(result_string)


def sub_b(string):
    if string == S:
        print(1)
        quit()

    if len(string) > len(S) and string[0] == 'B':
        result_string = string[1:]
        result_string = result_string[::-1]
        sub_a(result_string)
        sub_b(result_string)


S = input().rstrip()  # S: 바꿔야 하는 문자열
T = input().rstrip()  # T: 목표 문자열
input_T = T[:]

sub_a(input_T)
sub_b(input_T)

print(0)