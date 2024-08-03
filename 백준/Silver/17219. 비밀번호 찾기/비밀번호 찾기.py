import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # N: 사이트 주소 수, M: 비밀번호를 찾으려는 사이트 주소 수

data = {}

for _ in range(N):
    domain, pw = input().split()
    data[domain] = pw

for _ in range(M):
    domain_ = input().rstrip()
    print(data[domain_])