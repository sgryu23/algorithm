import sys

S = sys.stdin.readline().rstrip()
string_index = [0 for _ in range(26)]

for s in S:
    string_index[ord(s) - ord('a')] += 1

for i in string_index:
    print(i, end=" ")