import sys
input = sys.stdin.readline

N = int(input())
answer = 0
chat = set()

for _ in range(N):
    string = input().rstrip()
    if string == 'ENTER':
        chat.clear()
    else:
        if string in chat:
            continue
        else:
            chat.add(string)
            answer += 1

print(answer)