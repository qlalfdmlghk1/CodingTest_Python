# from heapq import heapify, heappush, heappop
# n = int(input())
# m = int(input())
# graph = [[]for _ in range(n+1)]
#
# for _ in range(m) :
#     u,v,s  = map(int,input().split())
#     graph[u].append((s,v))
#
# def cost(a,b) :
#     if a == b :
#         return 0
#     visited = [100001 for _ in range(n+1)]
#     answer = 0
#     pq = []
#     heappush(pq,(0,a))
#     while pq :
#         # print(pq)
#         cur = heappop(pq)
#         for nex in graph[cur[1]] :
#             nex_c, nex_v = nex[0],nex[1]
#             answer = cur[0] + nex_c
#             if visited[nex_v] > answer :
#                 visited[nex_v] = answer
#                 heappush(pq,(answer,nex_v))
#     if visited[b] == 100001 :
#         return 0
#     else :
#         return (visited[b])
#
# for i in range(1,n+1) :
#     for j in range(1,n+1) :
#         print(cost(i,j),end = ' ')
#     print()

#sol2)
# from heapq import heapify, heappush, heappop
# n = int(input())
# m = int(input())
# graph = [[]for _ in range(n+1)]
#
# for _ in range(m) :
#     u,v,s  = map(int,input().split())
#     graph[u].append((s,v))
#
# result = []
#
# def cost(a) :
#     visited = [100001 for _ in range(n+1)]
#     answer = 0
#     pq = []
#     heappush(pq,(0,a))
#     while pq :
#         # print(pq)
#         cur = heappop(pq)
#         for nex in graph[cur[1]] :
#             nex_c, nex_v = nex[0],nex[1]
#             answer = cur[0] + nex_c
#             if visited[nex_v] > answer :
#                 visited[nex_v] = answer
#                 heappush(pq,(answer,nex_v))
#     for i in range(1,n+1) :
#         if i == a :
#             visited[i] = 0
#     visited.pop(0)
#     result.append(visited)
#
# for i in range(1,n+1) :
#     cost(i)
# print(result)

#sol3)
n = int(input())
m = int(input())
graph = [[10001 for _ in range(n+1)]for _ in range(n+1)]

for i in range(1,n+1) :
    for j in range(1,n+1) :
        if i == j :
            graph[i][j] = 0

for _ in range(m) :
    u,v,s = map(int, input().split())
    graph[u][v] = min(s, graph[u][v])   # 노선이 하나가 아닐 수 있음 > 최소값 넣기


for k in range(1,n+1) :
    for a in range(1,n+1) :
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1,n+1) :
    for j in range(1,n+1) :
        if graph[i][j] == 10001 :
            print(0, end=' ')
        else :
            print(graph[i][j], end = ' ')
    print()

