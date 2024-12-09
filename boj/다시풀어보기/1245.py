from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
grid = []

for _ in range(n) :
    grid.append(list(map(int, input().split())))
visited = [[False for _ in range(m)] for _ in range(n)]
check_peak = [[False for _ in range(m)] for _ in range(n)]

dr = [1,1,1,0,0,0,-1,-1,-1]
dc = [1,0,-1,1,0,-1,1,0,-1]

answer = 0

def bfs(r,c) :
    global check_peak
    q = deque()
    q.append((r,c))
    point = grid[r][c]
    visited = [[False for _ in range(m)]for _ in range(n)]
    visited[r][c] = True
    while q :
        cur_r, cur_c = q.popleft()
        for i in range(8) :
            nex_r = cur_r + dr[i]
            nex_c = cur_c + dc[i]
            if 0 <= nex_r < n and 0 <= nex_c < m :
                if grid[nex_r][nex_c] == point and not visited[nex_r][nex_c]:
                    q.append((nex_r,nex_c))
                    check_peak[nex_r][nex_c] = True
                else :
                    if grid[nex_r][nex_c] > point :
                        return False
                visited[nex_r][nex_c] = True
    return True

for i in range(n) :
    for j in range(m) :
        if not visited[i][j] and grid[i][j] > 0 and not check_peak[i][j]:
            if bfs(i, j):
                answer += 1
                # print(i,j)

print(answer)
