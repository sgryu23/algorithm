import sys
input = sys.stdin.readline

# 단순 그리디는 시간 초과
# 유니온-파인드로 찾아야 함


def find_root(num):
    stack = [num]

    while True:
        parking = alt[num]
        if parking == num:
            break
        else:
            stack.append(parking)
            num = alt[parking]

    while stack:
        val = stack.pop()
        alt[val] = parking

    return parking


def union(root):
    b_root = find_root(root - 1)

    alt[root] = b_root


G = int(input())  # G: 게이트의 수
P = int(input())  # P: 비행기의 수
airplanes = [int(input()) for _ in range(P)]  # 비행기 번호 저장
alt = list(range(G + 1))  # 대안 게이트
ans = 0

for i in range(P):
    airplane = airplanes[i]
    root = find_root(airplane)

    if root == 0:
        break

    union(root)
    ans += 1

print(ans)