import sys

string = sys.stdin.readline().rstrip()
seconds = 0

for s in string:
    if s in 'ABC':
        seconds += 3
    elif s in 'DEF':
        seconds += 4
    elif s in 'GHI':
        seconds += 5
    elif s in 'JKL':
        seconds += 6
    elif s in 'MNO':
        seconds += 7
    elif s in 'PQRS':
        seconds += 8
    elif s in 'TUV':
        seconds += 9
    elif s in 'WXYZ':
        seconds += 10

print(seconds)