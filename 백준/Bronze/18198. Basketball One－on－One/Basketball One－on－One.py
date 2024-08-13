import sys

score = sys.stdin.readline().rstrip()
A_B = [0, 0]

for i in range(len(score)):
    if score[i] == 'A':
        A_B[0] += int(score[i + 1])
    elif score[i] == 'B':
        A_B[1] += int(score[i + 1])
    else:
        continue

if A_B[0] > 10 and A_B[0] - A_B[1] > 1:
    print('A')
elif A_B[1] > 10 and A_B[1] - A_B[0] > 1:
    print('B')