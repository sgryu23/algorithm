import sys
input = sys.stdin.readline

Ca, Ba, Pa = map(int, input().split())
Cr, Br, Pr = map(int, input().split())

ans = 0
if Cr - Ca > 0:
    ans += (Cr - Ca)
if Br - Ba > 0:
    ans += (Br - Ba)
if Pr - Pa > 0:
    ans += (Pr - Pa)
print(ans)