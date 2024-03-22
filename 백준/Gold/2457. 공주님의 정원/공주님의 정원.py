import sys
input = sys.stdin.readline

N = int(input())   # N: 꽃의 개수
answer = 0
arr = []

for i in range(N):
    s_month, s_day, f_month, f_day = map(int, input().split())   # s_month: 꽃이 피는 월, s_day: 꽃이 피는 일, f_month: 꽃이 지는 월, f_day: 꽃이 지는 일
    arr.append([s_month * 100 + s_day, f_month * 100 + f_day])

# arr 안의 값을 정렬
arr.sort(key=lambda x: (x[0], x[1]))

# 끝나는 날짜(start)를 찾아감
start = 301
end = 0

# 배열을 순회하면서 답 찾기
while arr:
    if start >= 1201 or arr[0][0] > start:
        break

    for i in range(len(arr)):
        if start >= arr[0][0]:
            if end <= arr[0][1]:
                end = arr[0][1]
            arr.remove(arr[0])
        else:
            break

    start = end
    answer += 1

if start < 1201:
    print(0)
else:
    print(answer)