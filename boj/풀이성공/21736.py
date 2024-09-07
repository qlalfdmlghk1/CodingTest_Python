from collections import deque
n, m = map(int, input().split())
q = deque()
graph = []
visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n) :
    graph.append(list(input()))

dr = [1,-1,0,0]
dc = [0,0,1,-1]
cnt = 0

def bfs(r,c) :
    global cnt
    q.append((r,c))
    while q :
        cur_r, cur_c = q.popleft()
        for i in range(4) :
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] != 'X' and visited[nr][nc] == False :
                if graph[nr][nc] == 'P' :
                    cnt += 1
                q.append((nr,nc))
                visited[nr][nc] = True
    if cnt == 0 :
        print('TT')
    else :
        print(cnt)

for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 'I' :
            visited[i][j] = True
            bfs(i,j)
