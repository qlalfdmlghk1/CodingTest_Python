import sys
input = sys.stdin.readline
from collections import deque
n,m = map(int,input().split())
visited = []
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

q = deque()
for _ in range(m) :
    v,u = map(int,input().split())
    graph[v].append(u)
    indegree[u] += 1

for v in range(1,n+1) :
    if indegree[v] == 0 :  # indegree == 0인 정점부터 시작
        q.append(v)
while q :
    cur = q.popleft()
    visited.append(cur)

    # 해당 정점과 연결된 노드들의 진입차수에서 1뺴기
    for nex in graph[cur] :
        indegree[nex] -= 1
        if indegree[nex] == 0 :
            q.append(nex)
print(*visited)