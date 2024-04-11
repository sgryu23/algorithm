def round2(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)


n = int(input())
if n > 0:
    grade_list = []
    for _ in range(n):
        grade_list.append(int(input()))
    
    grade_sum = 0
    grade_list.sort()
    fifteen_percent = round2(n * 0.15)
    for i in range(fifteen_percent, n - fifteen_percent):
        grade_sum += grade_list[i]
    ans = round2(grade_sum / (n - fifteen_percent * 2))
else:           # n이 0 이상 -> 이 때는 난이도 0으로 한다고 말해줬는데 놓쳤다.
    ans = 0
print(ans)