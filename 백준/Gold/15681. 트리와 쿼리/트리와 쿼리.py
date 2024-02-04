import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def count_subtree_nodes(current_node):
    children[current_node] = 1
    for j in trees[current_node]:
        if not children[j]:
            count_subtree_nodes(j)
            children[current_node] += children[j]


n, r, q = map(int, input().split())  # n: 트리 정점의 수, r: 루트 번호, q: 쿼리의 수
trees = [[] for _ in range(n + 1)]
children = [0] * (n + 1)

for i in range(n - 1):
    u, v = map(int, input().split())
    trees[u].append(v)
    trees[v].append(u)

count_subtree_nodes(r)

for l in range(q):
    u = int(input())
    print(children[u])