import sys
input = sys.stdin.readline

a = []
for i in input():
    a.append(i)
a.sort(reverse=True)
ans = ''
for i in a:
    ans += str(i)
print(ans)