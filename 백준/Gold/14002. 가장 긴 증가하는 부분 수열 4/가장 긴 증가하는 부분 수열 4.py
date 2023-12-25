import sys
input = sys.stdin.readline

# 아이디어
# 최장 길이랑 그 때의 수열 함께 구하기 -> 하려고 했으나 복잡해서 각각 출력하기로
# 최장 길이 수열은 이중 for 돌면서 이전 값이랑 비교해서 작으면 그 길이를 저장

N = int(input())
A = list(map(int, input().split()))
dp = [1] * N  # 최장 수열 길이를 저장할 dp 리스트

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)
ans = max(dp)
print(ans)

subsequence = []  # 정답 수열 저장할 배열
for k in range(N - 1, -1, -1):
    if dp[k] == ans:
        subsequence.append(A[k])
        ans -= 1

subsequence.reverse()
print(*subsequence)