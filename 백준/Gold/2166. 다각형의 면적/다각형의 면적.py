import sys
input = sys.stdin.readline

# 접근 방법
# 삼각형으로 분할해서 각각의 삼각형 넓이를 모두 더하는 것
# CCW 알고리즘이 쓰임(11758_CCW 참고)
# self-intersecting polygon 의 경우는 출력이 0이 나오는데 그 경우는 고려하지 않아도 될 듯
# CCW 코드 참고: https://ko.wikihow.com/%EB%8B%A4%EA%B0%81%ED%98%95-%EB%84%93%EC%9D%B4-%EA%B5%AC%ED%95%98%EA%B8%B0#:~:text=%EC%A0%95%EB%8B%A4%EA%B0%81%ED%98%95%EC%9D%98%20%EB%84%93%EC%9D%B4%EB%A5%BC%20%EA%B5%AC,%EC%9D%98%20%EC%A4%91%EC%8B%AC%EC%9C%BC%EB%A1%9C%20%EB%AA%A8%EC%9D%B4%EB%8A%94%20%EC%84%A0%EB%B6%84

x, y = [], []  # 각각의 x좌표, y좌표 담을 리스트 생성
N = int(input())  # N: 점의 개수
for _ in range(N):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)
x.append(x[0])
y.append(y[0])

area1, area2 = 0, 0

# CCW 공식으로 면적 1, 2를 구한 다음 (면적1 - 면적 2) / 2
for i in range(N):
    area1 += x[i] * y[i + 1]
    area2 += y[i] * x[i + 1]
ans = round(abs((area1-area2) / 2), 1)  # 소수점 첫째 자리까지 출력하라 했으므로
print(ans)