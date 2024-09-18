import sys
input = sys.stdin.readline

a, b = map(int, input().split())
x_old, y_old = (a + b) / 2, 2 * a * b / (a + b)

while True:
    x_new = round((x_old + y_old) / 2, 6)
    y_new = round(2 * x_old * y_old / (x_old + y_old), 6)

    if x_new == x_old and y_new == y_old:
        print(x_new, y_new)
        break

    x_old = x_new
    y_old = y_new
