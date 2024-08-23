import sys
s = list(sys.stdin.readline().rstrip())
power = 0
answer = 0
dic = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
    }

for i in range(len(s) - 1, -1, -1):
    if s[i] in 'ABCDEF':
        answer += (dic[s[i]] * (16 ** power))
    else:
        answer += int(s[i]) * (16 ** power)
    power += 1

print(answer)