import sys
input = sys.stdin.readline


def multiply(array_1, array_2):
    result = [[0 for _ in range(8)] for _ in range(8)]

    for i in range(8):
        for j in range(8):
            for k in range(8):
                result[i][j] += array_1[i][k] * array_2[k][j]
            result[i][j] %= mod

    return result


def cal(arr, n):
    if n == 1:
        return arr
    cal2 = cal(arr, n // 2)
    if n % 2 == 0:
        return multiply(cal2, cal2)
    else:
        return multiply(multiply(cal2, cal2), arr)


d = int(input())
mod = 1000000007

graph = [[0 for c in range(8)] for r in range(8)]

graph[0][1] = graph[0][2] = 1                              # 0: 정보과학관
graph[1][0] = graph[1][2] = graph[1][3] = 1                # 1: 전산관
graph[2][0] = graph[2][1] = graph[2][3] = graph[2][4] = 1  # 2: 미래관
graph[3][1] = graph[3][2] = graph[3][4] = graph[3][5] = 1  # 3: 신양관
graph[4][2] = graph[4][3] = graph[4][5] = graph[4][7] = 1  # 4: 한경직 기념관
graph[5][3] = graph[5][4] = graph[5][6] = 1                # 5: 진리관
graph[6][5] = graph[6][7] = 1                              # 6: 학생회관
graph[7][4] = graph[7][6] = 1                              # 7: 형남공학관

result = cal(graph, d)

print(result[0][0])