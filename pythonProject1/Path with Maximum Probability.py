# undirected weighted graph of n nodes (0-indexed)
# Given two nodes start and end,
# find the path with the maximum probability of success to go from start to end and
# return its success probability.
# If there is no path from start to end, return 0.
# Your answer will be accepted if it differs from the correct answer by at most 1e-5.
n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2
import heapq
graph = [[] for _ in range(n+1)]

pq = []
max_visited = [0] * (n+1)
max_visited[start] = 1
pq.append((-1,start))


for index,(u,v) in enumerate(edges) :
    graph[u].append((succProb[index],v))
    graph[v].append((succProb[index],u))

while pq :
    print(max_visited)
    cur_pro, cur_node = heapq.heappop(pq)
    for next_pro,next_node in graph[cur_node] :
        if -cur_pro * next_pro > max_visited[next_node] :
            max_visited[next_node] = -cur_pro * next_pro
            heapq.heappush(pq, (-max_visited[next_node],next_node))


print(max_visited[end])