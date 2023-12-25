import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)  # recursionError 방지


# 전위 순회 결과를 후위 순회로 바꿔서 출력해야 함
# 배열을 하나씩 넘어가면서 제일 앞에 있는 수는 루트 노드, 루트보다 작은 수는 왼쪽 배열, 큰 수는 오른쪽 배열

def make_postorder(lst):
    if len(lst) == 0:
        return

    subtree_left, subtree_right = [],  []
    mid = lst[0]  # 첫 번째 값이 루트(전위 순회 개념)
    # 왼쪽 서브 트리는 루트보다 작은 값, 오른쪽 서브 트리는 루트보다 큰 값(이진 검색 트리 개념)
    for n in range(1, len(lst)):
        if lst[n] > mid:
            subtree_left = lst[1:n]
            subtree_right = lst[n:]
            break
    else:  # 모든 노드의 값이 루트 값보다 작은 경우(예외)
        subtree_left = lst[1:]

    # 왼쪽, 오른쪽 순으로 재귀 후 루트 노드 값 출력
    make_postorder(subtree_left)
    make_postorder(subtree_right)
    print(mid)


arr = []

# 0. 입력값 받기
while True:
    try:
        node = int(input())
        arr.append(node)
    except:
        break

make_postorder(arr)