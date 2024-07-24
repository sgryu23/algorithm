import sys

s = sys.stdin.readline().rstrip()
answer = ''

for i in s:
    if i.islower():
        answer += i.upper()
    else:
        answer += i.lower()

print(answer)