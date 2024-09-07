import sys
s = sys.stdin.readline().rstrip()
left = 0
right = 0

for i in range(9):
    if s[i] in '123456789' and i != 8:
        left += int(s[i])
    if i == 8:
        right += int(s[i])

if left == right:
    print('YES')
else:
    print('NO')