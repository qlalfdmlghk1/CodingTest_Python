import sys
input = sys.stdin.readline
from heapq import heappop, heappush
v,e = map(int, input().split())
k = int(input())
graph =[[] for _ in range(v+1)]
for _ in range(e) :
    arr = list(map(int, input().split()))
    graph[arr[0]].append((arr[2],arr[1]))

distance = [0xffffff] * (v+1)
def dikstra(start) :
    pq = []
    pq.append((0,k))
    while pq :
        cur_distance, cur_node = heappop(pq)
        if distance[cur_node] < cur_distance :
            continue
        for next_distance, next_node in graph[cur_node] :
            sum_distance = cur_distance + next_distance
            if distance[next_node] > sum_distance :
                distance[next_node] = sum_distance
                heappush(pq,(sum_distance,next_node))

distance[k] = 0
dikstra(k)

for i in range(1,v+1) :
    if distance[i] >= 0xffffff :
        print('INF')
    else :
        print(distance[i])
