import sys
input = sys.stdin.readline

n = int(input())  # n: 테스트 케이스 개수
for i in range(n):
    p = int(input())  # p: 고려해야 할 선수
    max_price_name, max_price = None, 0
    for j in range(p):
        price, name = map(str, input().split())
        price = int(price)
        if price > max_price:
            max_price = price
            max_price_name = name
    print(max_price_name)