import heapq
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
graph = [[] for _ in range(n+1)]

for u,v,time in times :
    graph[u].append((time,v))

costs = {}
pq = []
heapq.heappush(pq,(0,k))

while pq :
    cur_cost, cur_node = heapq.heappop(pq)
    if cur_node not in costs : # 현재 노드가 방문한적이 없다면
        costs[cur_node] = cur_cost
        for cost,next_node in graph[cur_node] :
            next_cost = cur_cost + cost
            heapq.heappush(pq, (next_cost,next_node))

for node in range(1,n+1) :
    if node not in costs :
        print(-1)

print(max(costs.values()))
print(costs)