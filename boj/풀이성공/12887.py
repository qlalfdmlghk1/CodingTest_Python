from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
graph = []
dr = [0,1,-1]
dc = [1,0,0]

def bfs(r,c) :
    visited = [[0 for _ in range(n)] for _ in range(2)]
    q = deque()
    q.append((r,c))
    visited[r][c] = 1
    while q :
        cur_r, cur_c = q.popleft()
        if cur_c == n - 1:
            return visited[cur_r][cur_c]
        for i in range(3) :
            nex_r = cur_r + dr[i]
            nex_c = cur_c + dc[i]
            if 0 <= nex_r < 2 and 0 <= nex_c < n and graph[nex_r][nex_c] == "." and visited[nex_r][nex_c] == 0 :
                visited[nex_r][nex_c] = visited[cur_r][cur_c] + 1
                q.append((nex_r,nex_c))
    return 0

for _ in range(2) :
    graph.append(list(input().rstrip()))

cnt,cnt1,cnt2 = 0,101,101
for i in range(2) :
    for j in range(n) :
        if graph[i][j] == "." :
            cnt += 1

if graph[0][0] == "." :
    cnt1 = bfs(0,0)

if graph[1][0] == "." :
    cnt2 = bfs(1,0)

print(cnt - min(cnt1, cnt2))
