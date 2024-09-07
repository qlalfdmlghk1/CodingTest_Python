from collections import deque
n = int(input())
graph = []
visited = [[False for _ in range(n)] for _ in range(n)]
q = deque()

for i in range(n) :
    graph.append(list(input()))

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def bfs(r,c) :
    q.append((r,c))
    while q :
        cur_r, cur_c = q.popleft()
        for i in range(4) :
            nex_r = dr[i] + cur_r
            nex_c = dc[i] + cur_c
            if 0 <= nex_r < n and 0 <= nex_c < n and graph[cur_r][cur_c] == graph[nex_r][nex_c] and visited[nex_r][nex_c] == False:
                q.append((nex_r,nex_c))
                visited[nex_r][nex_c] = True

cnt1 = 0
for i in range(n) :
    for j in range(n):
        if visited[i][j] == False :
            bfs(i,j)
            cnt1 += 1

for i in range(n) :
    for j in range(n):
        if graph[i][j] == 'G' :
            graph[i][j] = 'R'

visited = [[False for _ in range(n)] for _ in range(n)]
cnt2 = 0
for i in range(n) :
    for j in range(n):
        if visited[i][j] == False :
            bfs(i,j)
            cnt2 += 1

print(cnt1,cnt2)