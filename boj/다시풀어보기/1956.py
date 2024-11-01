# v,e = map(int, input().split())

# def findSet(parents,a) :
#     if parents[a] != a :
#         parents[a] = findSet(parents,parents[a])
#     return parents[a]
#
# def union(parents,a,b) :
#     aRoot = findSet(parents,a)
#     bRoot = findSet(parents,b)
#     if aRoot < bRoot :
#         parents[aRoot] = bRoot
#     else :
#         parents[bRoot] = aRoot
#
# edges = []
# parents = [-1] * (v+1)
# result = 1
#
# for i in range(v+1) :
#     parents[i] = i
#
# for _ in range(e) :
#     a,b,c = map(int, input().split())
#     edges.append((c,a,b))
# edges.sort()
#
# for edge in edges :
#     c, a, b = edge
#     if findSet(parents,a) != findSet(parents,b) :
#         union(parents,a,b)
#         result += c
# print(result)

v,e = map(int, input().split())
answer = 1e9
# 거리를 저장할 graph
graph = [[int(1e9)] * (v+1) for _ in range(v+1)]
for _ in range(e) :
    a,b,c = map(int, input().split())
    graph[a][b] = c

for k in range(1, v+1) :
    for i in range(1, v+1) :
        for j in range(1, v+1) :
            if graph[i][k] + graph[k][j] < graph[i][j] :
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(1,v+1) :
    answer = min(answer, graph[i][i]) # i -> i까지의 거리 확인

if answer == 1e9 :
    print(-1)
else :
    print(answer)