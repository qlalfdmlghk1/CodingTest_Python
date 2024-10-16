maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
from collections import deque
n = len(maps)
m = len(maps[0])
dr = [1,-1,0,0]
dc = [0,0,1,-1]

def start_to_Label(start_r,start_c) :
    q = deque()
    q.append((start_r,start_c))
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    visited[start_r][start_c] = 0
    while q :
        cur_r,cur_c = q.popleft()
        for i in range(4) :
            nex_r = cur_r + dr[i]
            nex_c = cur_c + dc[i]
            if 0 <= nex_r < m and 0 <= nex_c < n and visited[nex_r][nex_c] == -1 and maps[nex_r][nex_c] != "X":
                if maps[nex_r][nex_c] == "L" :
                    return visited[cur_r][cur_c] + 1
                visited[nex_r][nex_c] = visited[cur_r][cur_c] + 1
                q.append((nex_r,nex_c))
    return -1


def label_to_exit(start_r, start_c):
    q = deque()
    q.append((start_r, start_c))
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    visited[start_r][start_c] = 0
    while q:
        cur_r, cur_c = q.popleft()
        for i in range(4):
            nex_r = cur_r + dr[i]
            nex_c = cur_c + dc[i]
            if 0 <= nex_r < m and 0 <= nex_c < n and visited[nex_r][nex_c] == -1 and maps[nex_r][nex_c] != "X":
                if maps[nex_r][nex_c] == "E":
                    return visited[cur_r][cur_c] + 1
                visited[nex_r][nex_c] = visited[cur_r][cur_c] + 1
                q.append((nex_r, nex_c))
    return -1

cnt1 = 0
cnt2 = 0

for i in range(n) :
    for j in range(m) :
        if maps[i][j] == "S" :
            cnt1 += start_to_Label(i, j)

for i in range(n) :
    for j in range(m) :
        if maps[i][j] == "L" :
            cnt2 += label_to_exit(i,j)

if cnt1 < 0 or cnt2 < 0 :
    print(-1)
else :
    print(cnt1+cnt2)