import sys

S = sys.stdin.readline().rstrip()
li = []

for i in range(len(S)):
    li.append(S[i:])

li.sort()

for j in range(len(S)):
    print(li[j])