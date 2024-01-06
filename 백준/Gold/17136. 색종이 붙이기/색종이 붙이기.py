import sys

# 1. 입력값 받기
input = sys.stdin.readline
board = [list(map(int, input().split())) for _ in range(10)]
papers = [0, 5, 5, 5, 5, 5]                      # 길이만큼 색종이가 각각 5개씩 있으니까 인덱스로 빼줄 예정
result = set()                                   # 결과 값을 담는데 중복 제거 & 처리 시간 단축을 위해 set 생성


# 2. 색종이 최대 길이 구하는 함수
def find_length(r, c):
    length = 1
    for lth in range(2, min(10 - r, 10 - c, 5) + 1):  # 델타 탐색으로 범위를 안 넘으면서 종이 길이는 최대 5까지 가능
        for i in range(r, r + lth):
            for j in range(c, c + lth):
                if board[i][j] == 0:
                    return length
        length += 1
    return length


# 3. 색종이 덮는 함수
def cover(r, c, length):
    for i in range(r, r + length):
        for j in range(c, c + length):          # length 만큼 1로 뒤덮인 곳 0으로 바꿈
            board[i][j] = 0


# 4. 색종이를 다시 원상 복구 시켜주는 함수
def uncover(r, c, length):
    for i in range(r, r + length):
        for j in range(c, c + length):           # 다시 나올 때 1로 바꿔줌
            board[i][j] = 1


def dfs(cnt):                                    # 변수는 색종이 총 개수
    for i in range(0, 10):
        for j in range(0, 10):
            if board[i][j] == 1:
                length = find_length(i, j)       # 1로 뒤덮인 길이만큼 반환
                for l in range(length, 0, -1):   # 길이가 긴 부분부터 length 1까지 탐색
                    if papers[l]:                # 해당 길이의 종이를 탐색
                        cover(i, j, l)
                        papers[l] -= 1             # 해당 길이만큼의 인덱스(색종이) 한 장 빼줌
                        result.add(dfs(cnt + 1))   # 색종이 개수 하나 더해주셈 & 재귀 탐색
                        uncover(i, j, l)
                        papers[l] += 1
                if result:
                    return min(result)
                else:
                    return -1
    return cnt


result.add(dfs(0))
if -1 in result:         # 재귀 함수를 썼으니까 -1이 생길 수밖에 없는데 해당 element 제거
    result.remove(-1)

if result:               # -1 제거 하고 result에 원소가 있으면 최소값 출력(최소 색종이 개수)
    print(min(result))
else:
    print(-1)