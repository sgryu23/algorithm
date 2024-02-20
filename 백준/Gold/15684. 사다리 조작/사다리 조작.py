# 아이디어 정리
# 두 가로선이 연속 X and 양 옆으로 나 있어도 안 된다.
# 완전탐색 & 백트래킹 dfs 방식으로 접근해야 할 듯? 조합인가?

# 1. 입력값 받기
cols, connected_rows, rows = map(int, input().split())   # cols: 세로선, connected_row: 연결된 가로선, rows: 가로선을 놓을 수 있는 위치의 개수
# [0] 으로 이뤄진 배열인데, 이어지는 지점만 1로 표시 -> 행을 하나씩 내려오면서 1을 만나면 옆 줄로 이동하도록 코드를 짤 예정
arr = [[0] * cols for _ in range(rows)]   # 0으로 이루어진 배열 생성(1부터 시작해서 세로, 가로 각각 + 1)
if connected_rows == 0:
    print(0)    # 연결된 가로 선이 없으면 그대로 내려오니까! (예외 처리)
    quit()
for _ in range(connected_rows):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = 1    # 사다리로 연결된 두 지점을 1로 표시(행을 하나씩 내려가면서 1이 있으면 양 옆으로 이동하게끔 코드를 설계

# 2. i 번째 세로선 결과 -> i 번이 나오는지 검증하는 함수
def is_same():
    for i in range(cols):  # 1번부터 cols 번까지 각 세로열이 자기 열에서 끝나는지 확인
        c = i  # 마지막에 행의 끝에 도달했을 때 그때 열과 같은지 비교해주기 위해 미리 값을 저장
        # 0번째 행에서 출발 -> rows번째 행까지 도착했을 때 열 값이 같은지(행, 열 값을 넣어서 최종 행에 도달했을 때 열이 어디인지 검증)
        for j in range(rows):
            if arr[j][c] == 1:  # 가로선이 있다면
                c += 1   # 가로선 오른쪽으로 이동
            elif c > 0 and arr[j][c - 1]:  # 가로선이 왼쪽에 있다면
                c -= 1    # 가로선 왼쪽으로 이동
        # 만약 rows까지 도달했다면 첫 시작했던 열과 같은지 비교
        if c != i:
            return False
    return True    # 끝까지 돌았는데 걸린 게 없었으면 True 반환


def dfs(row, col, cnt):  # cnt: 사다리 놔둔 횟수(함수 만들다가 추가)
    global ans
    # 종료 조건 구현
    if is_same():   # 시작 열과 끝 열이 같으면 최솟값 갱신 후 반환
        ans = min(ans, cnt)
        return
    elif cnt == 3 or ans <= cnt:   # 횟수가 3이 넘어가거나 최솟값을 넘어가면 가지치기
        return

    for rr in range(row, rows):
        if rr == row:       # 행이 같다면
            current = col   # 지금 탐색 중인 열부터 탐색
        else:               # 행이 변경된 경우
            current = 0     # 가로선 처음부터 탐색

        for cc in range(current, cols - 1):  # 열을 순회하면서 사다리 둘 곳 찾음
            if arr[rr][cc] == 0 and arr[rr][cc + 1] == 0:  # 탐색하는 열 두 군데 다 사다리가 없으면
                # 왼쪽에 사다리 존재하면 패스(문제 조건에서 주어짐)
                if cc > 0 and arr[rr][cc - 1] == 1:
                    continue
                arr[rr][cc] = 1   # 가로로 사다리 하나 놓기
                dfs(rr, cc + 2, cnt + 1)   # 연속한 사다리(--) 놓을 수 X -> 열은 2를 건너 뛰어서 재귀함수(이 부분을 생각을 못 함)
                arr[rr][cc] = 0   # 백트래킹(사다리 치우기)


ans = 4   # 4 미만인 경우에만 답 출력
dfs(0, 0, 0)
if ans < 4:
    print(ans)
else:
    print(-1)