import sys
input = sys.stdin.readline

from collections import deque
n,m,k,x = map(int, input().split())

answer = []
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]  # 시작점 x -> x의 거리가 0이므로

for _ in range(m) :
    a,b = map(int,input().split())
    graph[a].append(b)  # 단방향 이므로

def bfs(v) :    # bfs 수행
    q = deque()
    q.append(v)
    while q :
        cur = q.popleft()
        for nex in graph[cur] :
            if visited[nex] == False :
                visited[nex] = visited[cur] + 1
                q.append(nex)


bfs(x)

visited[x] = 0  # 틀렸습니다 원인 -> 시작 지점은 거리가 0 이므로

for ind,distance in enumerate(visited) :
    if distance == k :
        answer.append(ind)

if not answer :
    print(-1)
else :
    answer.sort()
    for i in answer :
        print(i)