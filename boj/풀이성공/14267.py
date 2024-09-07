from collections import deque
n,m = map(int, input().split())
relation = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
compliment = [0 for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for idx,r in enumerate(relation) :
    graph[r].append(idx+1)

for k in range(m) :
    i,w = map(int, input().split()) # 직속 상사로부터 칭찬을 받은 직원 번호 i, 칭찬의 수치 w
    compliment[i] += w

q = deque()
def bfs(v) :
    q.append(v)
    while q :
        cur = q.popleft()
        visited[cur] = True
        for nex in graph[cur] :
            if not visited[nex] :
                compliment[nex] += compliment[cur]
                q.append(nex)


for idx, p in enumerate(relation) :
    if p == -1 :
        bfs(idx+1)

print(*compliment[1:])
