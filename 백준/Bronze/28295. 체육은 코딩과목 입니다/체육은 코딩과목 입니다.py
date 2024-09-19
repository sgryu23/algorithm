import sys

initial = 0

for i in range(10):
    n = int(sys.stdin.readline())
    initial += n

answer = initial % 4
if answer == 0:
    print('N')
elif answer == 1:
    print('E')
elif answer == 2:
    print('S')
else:
    print('W')