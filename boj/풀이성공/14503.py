from collections import deque
n,m = map(int, input().split())
r,c,d = map(int, input().split())
dr = [-1,0,1,0]
dc = [0,-1,0,1]
graph = []
for i in range(n) :
    graph.append(list(map(int,map(int,input().split()))))

if d == 1:
    d = 3
elif d == 3 :
    d = 1

cnt = 0
q = deque()
q.append((r,c,d))

while q :
    cur_r, cur_c, cur_d = q.popleft()

    flag = False
    if graph[cur_r][cur_c] == 0 :
        cnt += 1
        graph[cur_r][cur_c] = 2
    for i in range(1,5) :
        flag = False
        nd = (cur_d + i) % 4
        nr = cur_r + dr[nd]
        nc = cur_c + dc[nd]
        if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 0 :
            cnt += 1
            graph[nr][nc] = 2
            q.append((nr,nc,nd))
            flag = True
            break
    if flag == False :
        nr = cur_r - dr[cur_d]
        nc = cur_c - dc[cur_d]
        if 0 <= nr < n and 0 <= nc < m :
            if graph[nr][nc] == 1 :
                print(cnt)
                exit()
            elif graph[nr][nc] == 0 :
                cnt += 1
                q.append((nr,nc,cur_d))
            elif graph[nr][nc] == 2 :
                q.append((nr, nc, cur_d))
        else :
            print(cnt)
            exit()