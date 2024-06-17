import sys

ppap = sys.stdin.readline().rstrip()

if ppap == 'P' or ppap == 'PPAP':
    print('PPAP')
else:
    stack = []
    element = ['P', 'P', 'A', 'P']
    for s in ppap:
        stack.append(s)
        if stack[-4:] == element:
            for _ in range(3):
                stack.pop()

    if stack == element or stack == ['P']:
        print('PPAP')
    else:
        print('NP')