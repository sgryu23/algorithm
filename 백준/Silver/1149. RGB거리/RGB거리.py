N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

for i in range(1, N):
    # 1. col == 0 선택
    arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0]
    # 2. col == 1 선택
    arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + arr[i][1]
    # 3. col == 2 선택
    arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + arr[i][2]

print(min(arr[N-1]))