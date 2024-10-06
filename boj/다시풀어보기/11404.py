# n = int(input())
# m = int(input())
# graph = [[10001 for _ in range(n+1)]for _ in range(n+1)]
#
# for i in range(1,n+1) :
#     for j in range(1,n+1) :
#         if i == j :
#             graph[i][j] = 0
#
# for _ in range(m) :
#     u,v,s = map(int, input().split())
#     graph[u][v] = min(s, graph[u][v])   # 노선이 하나가 아닐 수 있음 > 최소값 넣기
#
#
# for k in range(1,n+1) :
#     for a in range(1,n+1) :
#         for b in range(1, n+1):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
#
# for i in range(1,n+1) :
#     for j in range(1,n+1) :
#         if graph[i][j] == 10001 :
#             print(0, end=' ')
#         else :
#             print(graph[i][j], end = ' ')
#     print()

n = int(input())  # 도시의 개수
m = int(input())  # 버스의 개수


def findSet(parents,a) :
    if parents[a] != a :
        parents[a] = findSet(parents, parents[a])
    return parents[a]

def union(parents,a,b) :
    aRoot = findSet(parents, a)
    bRoot = findSet(parents, b)
    if aRoot < bRoot :
        parents[bRoot] = aRoot
    elif bRoot < aRoot :
        parents[aRoot] = bRoot


parents = [0] * (n+1)
edges = []
result = 0

for i in range(1,n+1) :
    parents[i] = i

for _ in range(m) :
    a,b,c = map(int, input().split())
    edges.append((c,a,b))
edges.sort()

for edge in edges :
    c,a,b = edge
    if findSet(parents,a) != findSet(parents,b) :
        union(parents,a,b)
        result += c
