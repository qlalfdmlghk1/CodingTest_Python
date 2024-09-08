# m,n = map(int, input().split())  #격자 크기, 순서대로 방문해야 하는 칸 수
# grid = []
# dr = [1,-1,0,0]
# dc = [0,0,1,-1]
# cnt = 0
#
# for _ in range(n) :
#     grid.append(list(map(int, input().split())))
#
# for _ in range(m) :
#     a,b = map(int, input().split())
#     grid[a-1][b-1] = 2
#
# def DFS(startR,startC,endR,endC,cnt) :
#     if startR == endR and startC == endC :
#         cnt += 1
#
#     for i in range(4) :
#         nexR = startR + dr[i]
#         nexC = startC + dc[i]


n,m = map(int, input().split())  #격자 크기, 순서대로 방문해야 하는 칸 수
grid = []
dest = []
for _ in range(n) :
    grid.append(list(map(int, input().split())))
for _ in range(m) :
    x,y = map(int, input().split())
    dest.append([x-1,y-1])
visited = [[False for _ in range(n)] for _ in range(n)]

#DFS로 풀 것임
cnt = 0
dr = [1,-1,0,0]
dc = [0,0,1,-1]

def dfs(now, destIdx) :
    global cnt
    if now == dest[destIdx] :
        if destIdx == m-1 :
            cnt += 1
            return
        else :
            destIdx += 1
    r,c = now
    visited[r][c] = True
    for i in range(4) :
        nr,nc = r + dr[i], c + dc[i]
        if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == False and grid[nr][nc] == 0 :
            dfs([nr,nc],destIdx)
    visited[r][c] = False
    return

dfs(dest[0],1)
print(cnt)