from collections import deque
n,m = map(int, input().split())
picture = []
visited = [[False for _ in range(m)] for _ in range(n)]
for _ in range(n) :
    picture.append(list(map(int, input().split())))

answer = []
def bfs(r,c) :
    global answer
    area = 1
    q = deque()
    q.append((r,c))
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    visited[r][c] = True
    while q :
        cur_r,cur_c = q.popleft()
        for i in range(4) :
            nex_r = cur_r + dr[i]
            nex_c = cur_c + dc[i]
            if 0 <= nex_r < n and 0 <= nex_c < m and not visited[nex_r][nex_c] and picture[nex_r][nex_c] == 1 :
                q.append((nex_r,nex_c))
                visited[nex_r][nex_c] = True
                area += 1
    answer.append(area)
    return True

cnt = 0
for i in range(n) :
    for j in range(m) :
        if picture[i][j] == 1 and not visited[i][j]:
            if bfs(i,j) :
                cnt += 1
answer.sort(reverse=True)
print(cnt)
if answer :
    print(answer[0])
else :
    print(0)