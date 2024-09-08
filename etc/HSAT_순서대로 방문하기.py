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
dest = []  # 방문해야 하는 목적지
visited = [[False for _ in range(n)] for _ in range(n)]

for _ in range(n) :
    grid.append(list(map(int, input().split())))
for _ in range(m) :
    x,y = map(int, input().split())
    dest.append([x-1,y-1])


#DFS로 풀 것임
cnt = 0
dr = [1,-1,0,0]
dc = [0,0,1,-1]

def dfs(now, destIdx) :  # now : 현재 리스트
    global cnt
    if now == dest[destIdx] :
        if destIdx == m-1 :  # 마지막 목적지까지 도달했으면 cnt++ && return
            cnt += 1
            return
        else :               # 중간 경유 목적지에 도달했다면
            destIdx += 1     # 경유 인덱스 +1
    cur_r,cur_c = now
    visited[cur_r][cur_c] = True

    for i in range(4) :
        nex_r = cur_r + dr[i]
        nex_c = cur_c + dc[i]
        if (0 <= nex_r < n and 0 <= nex_c < n
                and visited[nex_r][nex_c] == False and grid[nex_r][nex_c] == 0) :
            dfs([nex_r,nex_c],destIdx)
    visited[cur_r][cur_c] = False
    return

dfs(dest[0],1)
print(cnt)