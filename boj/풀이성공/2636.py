from collections import deque
n,m = map(int, input().split())
grid = []
for _ in range(n) :
    grid.append(list(map(int,input().split())))

total = 0
for r in range(n) :
    for c in range(m) :
        if grid[r][c] == 1 :
            total += 1

def bfs() :
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    cheese = deque()
    q.append((0,0))
    dr = [1,-1, 0, 0]
    dc = [0, 0, 1, -1]
    cnt = 0
    while q :
        cur_r, cur_c = q.popleft()
        for i in range(4) :
            nex_r = cur_r + dr[i]
            nex_c = cur_c + dc[i]
            if 0 <= nex_r < n and 0 <= nex_c < m:
                if grid[nex_r][nex_c] == 0 and not visited[nex_r][nex_c]:
                    visited[nex_r][nex_c] = True
                    q.append((nex_r, nex_c))
                elif grid[nex_r][nex_c] == 1 and not visited[nex_r][nex_c]:
                    visited[nex_r][nex_c] = 1
                    cheese.append((nex_r,nex_c))

    while cheese :
        c1,c2 = cheese.popleft()
        grid[c1][c2] = 0
        cnt += 1
    return cnt

answer = 0
cheese_cnt = []
cheese_cnt.append(total)

while total > 0 :
    total -= bfs()
    cheese_cnt.append(total)
    answer += 1
print(answer)
print(cheese_cnt[answer-1])




