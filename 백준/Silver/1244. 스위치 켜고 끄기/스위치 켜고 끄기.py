num = int(input())
switch = list(map(int, input().split()))
student = int(input())

for n in range(student):
    sex, card = map(int, input().split())
    if sex == 1:
        for i in range(num):
            times = (i+1) * card - 1
            if 0 <= times < num:
                if switch[times] == 1:
                    switch[times] = 0
                else:
                    switch[times] = 1
    elif sex == 2:
        fem_idx = card-1
        if switch[fem_idx] == 0:
            switch[fem_idx] = 1
        else:
            switch[fem_idx] = 0
        for k in range(1, num):
            if 0 <= fem_idx-k < num and 0 <= fem_idx+k < num:
                if switch[fem_idx-k] == 0 and switch[fem_idx+k] == 0:
                    switch[fem_idx-k] = 1
                    switch[fem_idx+k] = 1
                elif switch[fem_idx-k] == 1 and switch[fem_idx+k] == 1:
                    switch[fem_idx-k] = 0
                    switch[fem_idx+k] = 0
                else:
                    break

ans = []
idx = 0
while num >= idx:
    ans.append(switch[idx:idx+20])
    idx += 20

for a in ans:
    print(' '.join(map(str, a)))