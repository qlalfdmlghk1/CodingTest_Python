n, m, x = map(int, input().split())  # n: 노드 수, m: 간선 수, x: 특정 노드

up   = [[] for _ in range(n + 1)]
down = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    down[a].append(b)  # a 아래에 b가 있음
    up[b].append(a)    # b 위에 a가 있음

visited = [False] * (n + 1)

def dfs(x, graph, cnt):
    visited[x] = True
    cnt[0] += 1           # 현재 노드를 포함한 카운트 증가
    for nex in graph[x]:  # 현재 노드와 연결된 모든 노드에 대해
        if not visited[nex]:
            dfs(nex, graph, cnt)

upNode = [-1]    # upNode   : 상위 노드의 개수를 저장
downNode = [-1]  # downNode : 하위 노드의 개수를 저장
dfs(x, up, upNode)      # x를 기준으로 상위 노드 탐색
dfs(x, down, downNode)  # x를 기준으로 하위 노드 탐색

print(1 + upNode[0], end=" ")
print(n - downNode[0])
