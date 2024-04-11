from collections import deque


def double(num):
    n = (num * 2) % 10000
    return n


def subtract(num):
    if num == 0:
        n = 9999
    else:
        n = num - 1
    return n


def left(num):
    return num // 1000 + (num % 1000) * 10


def right(num):
    return num // 10 + (num % 10) * 1000


for _ in range(int(input())):
    A, B = map(int, input().split())
    visited = set()
    q = deque()
    visited.add(A)
    q.append((A, ''))

    while q:
        num1, com = q.popleft()
        if num1 == B:
            print(com)
            break
        D_num = double(num1)
        if D_num not in visited:
            visited.add(D_num)
            q.append((D_num, com + 'D'))

        S_num = subtract(num1)
        if S_num not in visited:
            visited.add(S_num)
            q.append((S_num, com + 'S'))

        L_num = left(num1)
        if L_num not in visited:
            visited.add(L_num)
            q.append((L_num, com + 'L'))

        R_num = right(num1)
        if R_num not in visited:
            visited.add(R_num)
            q.append((R_num, com + 'R'))