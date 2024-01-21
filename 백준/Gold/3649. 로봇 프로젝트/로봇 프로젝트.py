import sys
input = sys.stdin.readline

while True:
    try:
        # 1. 값 입력 => 없으면 except 에서 예외처리
        x = int(input()) * 10000000  # x: 구멍의 너비(cm == 10,000,000 nm)
        n = int(input())  # n: 레고 조각의 수
        legos = []
        for lego in range(n):
            l = int(input())  # l: 레고 조각의 길이(nm)
            legos.append(l)

        # 2. 레고 정렬
        legos.sort()  # 정렬해서 오름차순이면 |l1 - l2| 값이 가장 큰 것을 출력함
        left, right = 0, n - 1
        answer_found = False
        while left < right:
            if legos[left] + legos[right] == x:
                print(f'yes {legos[left]} {legos[right]}')
                answer_found = True
                break
            # x 보다 작은 경우 -> left 를 한 칸 오른쪽으로 옮김
            elif legos[left] + legos[right] < x:
                left += 1
            # x 보다 큰 경우 -> right 를 한 칸 왼쪽으로 옮김
            else:
                right -= 1
        if not answer_found:
            print('danger')
    except:
        break