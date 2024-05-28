import sys
input = sys.stdin.readline

N = int(input())  # N: 메뉴의 수
menus = [0]
answer = 0

for _ in range(N):
    price = int(input())
    menus.append(price)

M = int(input())  # M: 인원 수
for i in range(M):
    menu_number = int(input())
    answer += menus[menu_number]

print(answer)