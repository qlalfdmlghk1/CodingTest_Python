import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, r, q = map(int,input().split())

# 그냥 DFS 임?
graph = [[] for _ in range(n+1)]

for _ in range(n-1) :
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)
cnt = [1] * (n+1)
visited[r] = True

def dfs(start) :
    if not graph[start] :
        return 1

    for nex in graph[start] :
        if not visited[nex] :
            # print(start, cnt, nex)
            visited[nex] = True
            cnt[start] += dfs(nex)
    return cnt[start]

dfs(r)

for _ in range(q) :
    s = int(input())
    print(cnt[s])