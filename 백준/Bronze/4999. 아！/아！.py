import sys
input = sys.stdin.readline

j_input = input()
d_input = input()

if len(j_input) >= len(d_input):
    print('go')
else:
    print('no')