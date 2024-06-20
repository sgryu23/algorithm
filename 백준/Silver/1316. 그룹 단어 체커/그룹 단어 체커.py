import sys
input = sys.stdin.readline

N = int(input())
answer = N

for i in range(N):
    word = input().rstrip()
    for j in range(len(word) - 1):
        if word[j] == word[j + 1]:
            pass
        elif word[j] in word[j + 1:]:
            answer -=1
            break

print(answer)