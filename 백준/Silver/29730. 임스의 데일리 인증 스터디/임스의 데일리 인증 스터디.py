import sys
input = sys.stdin.readline

N = int(input())
records = []
boj = []

for _ in range(N):
    record = input().rstrip()
    if record.startswith('boj.kr/'):
        boj.append(record)
    else:
        records.append(record)

if records:
    records.sort(key=lambda x: (len(x), x))
boj.sort(key=lambda x: int(x[7:]))

for i in range(len(records)):
    print(records[i])

for j in range(len(boj)):
    print(boj[j])