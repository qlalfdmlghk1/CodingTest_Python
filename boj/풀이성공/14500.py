# 풀이 완전 이해 후 혼자서 풀어본 풀이
# 다음엔 무조건 한번에 푼다..!
import sys
input = sys.stdin.readline
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

n,m = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

maxValue = 0

def dfs(r,c,dsum, cnt) :
    global maxValue
    if cnt == 4 :
        maxValue = max(maxValue,dsum)
        return
    else :
        for i in range(4) :
            nex_r = r + dr[i]
            nex_c = c + dc[i]
            if (0 <= nex_r < n and 0 <= nex_c < m and visited[nex_r][nex_c] == False) :
                visited[nex_r][nex_c] = True
                dfs(nex_r,nex_c,dsum+board[nex_r][nex_c],cnt+1)
                visited[nex_r][nex_c] = False

from itertools import combinations

def exec(r,c) :
    global maxValue
    tmp = board[r][c]
    arr = [0,1,2,3]
    for k in combinations(arr,3) :
        for i in range(3) :
            nex_r = r + dr[k[i]]
            nex_c = c + dc[k[i]]
            if not (0 <= nex_r < n and 0 <= nex_c < m) :
                tmp = 0
                break
            tmp += board[nex_r][nex_c]
        maxValue = max(maxValue, tmp)
        tmp = 0

for i in range(n) :
    for j in range(m):
        if visited[i][j] == False :
            visited[i][j] = True
            dfs(i,j,board[i][j],1)
            visited[i][j] = False

        exec(i,j)
print(maxValue)