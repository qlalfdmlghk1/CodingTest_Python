from collections import deque

n,m = map(int,input().split())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
q = deque()
for _ in range(m) :
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(v) :
    q.append(v)
    visited[v] = True
    while q :
        cur = q.popleft()
        for nex in graph[cur] :
            if visited[nex] == False :
                visited[nex] = True
                q.append(nex)

cnt = 0

for i in range(1,n+1) :
    if visited[i] == False :
        bfs(i)
        cnt += 1
print(cnt)