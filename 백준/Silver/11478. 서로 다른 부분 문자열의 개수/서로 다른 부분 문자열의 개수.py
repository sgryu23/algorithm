import sys
sys.setrecursionlimit(10 ** 4)

def func(sub_string, idx, initial_idx):
    sub_string += S[idx]
    strings.add(sub_string)
    if len(sub_string) + initial_idx == len(S):
        return
    func(sub_string, idx + 1, initial_idx)


S = sys.stdin.readline().rstrip()
strings = set()

for i in range(len(S)):
    substring = ''
    func(substring, i, i)

print(len(strings))