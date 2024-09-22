import sys
input = sys.stdin.readline

retake = input().rstrip()
N = int(input())
answer = 0

for _ in range(N):
    input_ = input().rstrip()
    if retake[:5] == input_[:5]:
        answer += 1

print(answer)