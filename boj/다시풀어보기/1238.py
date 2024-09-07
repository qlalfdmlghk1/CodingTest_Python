# 풀이1)
# import sys
# input = sys.stdin.readline
# from collections import deque
# n,m,x = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# q = deque()
#
# for _ in range(m) :
#     student = list(map(int, input().split()))
#     graph[student[0]].append((student[1],student[2]))
# def back(town) :
#     street = 21470000
#     q.append((2, 0))
#     visited = [False] * (m + 1)
#     visited[2] = True
#     while q:
#         cur_town, cur_street = q.popleft()
#         for nex_town, nex_street in graph[cur_town]:
#             if visited[nex_town] == False:
#                 sum_street = cur_street + nex_street
#                 if nex_town == town:
#                     street = min(street, sum_street)
#                 else:
#                     visited[nex_town] = True
#                     q.append((nex_town, sum_street))
#     return street
#
# def bfs(town) :
#     street = 21470000
#     q.append((town,0))
#     visited = [False] * (m+1)
#     visited[town] = True
#     while q :
#         cur_town,cur_street = q.popleft()
#         for nex_town, nex_street in graph[cur_town] :
#             print(q)
#             if visited[nex_town] == False :
#                 sum_street = cur_street + nex_street
#                 if nex_town == x :
#                     street = min(street, sum_street)
#                 else :
#                     visited[nex_town] = True
#                     q.append((nex_town,sum_street))
#     return street
#
# total = []
# for i in range(1,n+1) :
#     if i != x :
#         total.append(bfs(i)+back(i))
#         print(bfs(i),back(i))
#
# print(max(total))

# 풀이2)
import sys
input = sys.stdin.readline
from heapq import heappop, heappush
from collections import deque
n,m,x = map(int, input().split())
graph = [[] for _ in range(n+1)]


for _ in range(m) :
    student = list(map(int, input().split()))
    graph[student[0]].append((student[2],student[1]))
# graph = [[], [(4, 2), (2, 3), (7, 4)], [(1, 1), (5, 3)], [(2, 1), (4, 4)], [(3, 2)]]
def dikstra(start) :
    hq = []
    distance = [21470000] * (n+1)
    heappush(hq,(0, start))
    distance[start] = 0
    while hq :
        cur_distance,cur_node = heappop(hq)
        if distance[cur_node] < cur_distance :
            continue
        for next_distance, next_node in graph[cur_node] :
            cost = cur_distance + next_distance
            if distance[next_node] > cost :
                distance[next_node] = cost
                heappush(hq,(cost,next_node))
    return distance


result = 0
for i in range(1,n+1) :
    go = dikstra(i)
    back = dikstra(x)
    result = max(result, go[x]+back[i])

print(result)