from collections import deque
n,m = map(int,input().split())
graph = []
visited = [[0 for _ in range(m)] for _ in range(n)]
q = deque()

for i in range(n) :
    graph.append(list(map(int,input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(r,c) :
    while q :
        cur_y, cur_x = q.popleft()
        for i in range(4) :
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == 0 and graph[ny][nx] == 1 :
                visited[ny][nx] = visited[cur_y][cur_x] + 1
                q.append((ny,nx))

for i in range(n) :
    for j in range(m):
        if graph[i][j] == 2 :
            q.append((i,j))
            visited[i][j] = 0
            bfs(i,j)

for i in range(n) :
    for j in range(m):
        if visited[i][j] == 0 and graph[i][j] == 1 :
            visited[i][j] = -1
for i in range(n):
    for j in range(m):
        print(visited[i][j], end = ' ')
    print()