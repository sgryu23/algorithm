import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    size = int(input())
    password = input().rstrip()
    if size >= 12:
        lower_case = False
        upper_case = False
        digit = False
        symbol = False
        for i in password:
            if i in 'abcdefghijklmnopqrstuwxyz' and not lower_case:
                lower_case = True
            elif i in 'ABCDEFGHIJKLMNOPQRSTUWXYZ' and not upper_case:
                upper_case = True
            elif i in '1234567890' and not digit:
                digit = True
            elif i in '+_)(*&^%$#@!./,;{}' and not symbol:
                symbol = True
        if lower_case and upper_case and digit and symbol:
            print('valid')
            continue
    print('invalid')