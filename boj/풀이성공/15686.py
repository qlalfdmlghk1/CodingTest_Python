import sys
input = sys.stdin.readline
from itertools import combinations

n,m = map(int, input().split())
graph = []
for _ in range(n) :
    graph.append(list(map(int,input().split())))

chickens = []
houses = []
for i in range(n) :
    for j in range(n):
        if graph[i][j] == 2 :
            chickens.append((i,j))
        if graph[i][j] == 1 :
            houses.append((i,j))

answer = 1e6
for chick in combinations(chickens,m) :
    sum = 0
    for house in houses :
        dis = int(1e6)
        for c in chick :
            dis = min(dis,abs(c[0]-house[0])+abs(c[1]-house[1]))
        sum += dis
    answer = min(answer,sum)

print(answer)



# import sys
# input = sys.stdin.readline
# from itertools import combinations
# from collections import deque
#
# n,m = map(int, input().split())
# city = []
# chicken = []
# cnt = 0
#
# for _ in range(n) :
#     city.append(list(map(int,input().split())))
#
# for i in range(n) :
#     for j in range(n):
#         if city[i][j] == 2 :
#             chicken.append((i,j))
#             cnt += 1
#
# def bfs(r,c) :
#     visited = [[False for _ in range(n)] for _ in range(n)]
#     q = deque()
#     dr = [1,-1,0,0]
#     dc = [0,0,1,-1]
#     visited[r][c] = True
#     q.append((r,c))
#     while q :
#         cur_r, cur_c = q.popleft()
#         for i in range(4) :
#             nex_r = cur_r + dr[i]
#             nex_c = cur_c + dc[i]
#             if 0 <= nex_r < n and 0 <= nex_c < n and not visited[nex_r][nex_c] :
#                 if city[nex_r][nex_c] == 2:
#                     return (abs(nex_r-r) + abs(nex_c-c))
#                 visited[nex_r][nex_c] = True
#                 q.append((nex_r,nex_c))
#
#
# result = 1e9
# answer = 0
# if m == cnt :
#     for i in range(n):
#         for j in range(n):
#             if city[i][j] == 1:
#                 answer += bfs(i, j)
#
# for chi in combinations(chicken,cnt-m) :
#     for c in chi :
#         answer = 0
#         city[c[0]][c[1]] = 0
#         for i in range(n) :
#             for j in range(n) :
#                 if city[i][j] == 1 :
#                     answer += bfs(i,j)
#     result = min(answer, result)
#
#     for c in chi :
#         city[c[0]][c[1]] = 2
# print(result)