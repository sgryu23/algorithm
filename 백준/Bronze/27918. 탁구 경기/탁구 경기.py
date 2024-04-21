import sys
input = sys.stdin.readline

N = int(input())
Dalgu = 0
Phonix = 0
keep_going = True

for _ in range(N):
    winner = input().rstrip()
    if keep_going:
        if winner == 'D':
            Dalgu += 1
        else:
            Phonix += 1

    if abs(Dalgu - Phonix) == 2:
        keep_going = False

print(f'{Dalgu}:{Phonix}')