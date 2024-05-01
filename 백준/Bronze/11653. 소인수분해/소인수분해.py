n = int(input())

if n == 1:
    quit()

answer = []
dividend = 2
for i in range(n):
    if n % dividend == 0:
        answer.append(dividend)
        n //= dividend
    else:
        dividend += 1

for k in answer:
    print(k)
