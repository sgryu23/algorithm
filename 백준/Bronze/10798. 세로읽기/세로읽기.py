import sys
input = sys.stdin.readline

line1 = list(input().rstrip())
line2 = list(input().rstrip())
line3 = list(input().rstrip())
line4 = list(input().rstrip())
line5 = list(input().rstrip())

answer = ''

for i in range(max(len(line1), len(line2), len(line3), len(line4), len(line5))):
    if i < len(line1):
        answer += line1[i]
    if i < len(line2):
        answer += line2[i]
    if i < len(line3):
        answer += line3[i]
    if i < len(line4):
        answer += line4[i]
    if i < len(line5):
        answer += line5[i]

print(answer)