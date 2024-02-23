from collections import deque


def solution(land):
    n = len(land)
    m = len(land[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    check = set()
    dp = [0 for _ in range(m)]
    
    for row in range(n):
        for col in range(m):
            if land[row][col] == 1 and visited[row][col] == 0:
                check.add(col)
                volume = 1
                dq = deque()
                dq.append((row, col))
                visited[row][col] = 1

                while dq:
                    now_r, now_c = dq.popleft()
                    
                    for new_r, new_c in [(now_r - 1, now_c), (now_r, now_c + 1), (now_r + 1, now_c), (now_r, now_c - 1)]:
                        if 0 <= new_r < n and 0 <= new_c < m and land[new_r][new_c] == 1 and visited[new_r][new_c] == 0:
                            volume += 1
                            check.add(new_c)
                            dq.append((new_r, new_c))
                            visited[new_r][new_c] = 1
                
                for column in check:
                    dp[column] += volume
                
                check.clear()
                
    answer = max(dp)

    return answer