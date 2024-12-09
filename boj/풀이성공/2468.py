from collections import deque
n = int(input())
graph = []
for _ in range(n) :
    graph.append(list(map(int, input().split())))

def rain_height(x) :
    global visited
    for i in range(n) :
        for j in range(n) :
            if graph[i][j] <= x :
                visited[i][j] = True

dr = [1,-1,0,0]
dc = [0,0,1,-1]
def bfs(r,c) :
    global visited
    global result
    q = deque()
    q.append((r,c))
    while q :
        cur_r, cur_c = q.popleft()
        for i in range(4) :
            nex_r = cur_r + dr[i]
            nex_c = cur_c + dc[i]
            if 0 <= nex_r < n and 0 <= nex_c < n and not visited[nex_r][nex_c]:
                q.append((nex_r,nex_c))
                visited[nex_r][nex_c] = True
    result += 1

answer = 0
for h in range(100) :
    visited = [[False for _ in range(n)] for _ in range(n)]
    rain_height(h)
    result = 0
    for i in range(n) :
        for j in range(n) :
            if not visited[i][j] :
                bfs(i,j)
    # print(answer)
    answer = max(answer, result)
print(answer)

