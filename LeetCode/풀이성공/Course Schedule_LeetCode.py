numCourses = 1
prerequisites = []

#[ai, bi] indicates that you must take course bi first if you want to take course ai.
#모든 강의 다 들을 수 있으면 true, 아니면 false
from collections import deque
graph = [[] for _ in range(numCourses)]
visited = []
indegree = [0] * (numCourses)
for u,v in prerequisites :
    graph[v].append(u)
    indegree[u] += 1

q = deque()
for index,indeg in enumerate(indegree) :
    if indeg == 0 :
        q.append(index)
        visited.append(index)
print(graph)

while q :
    cur_node = q.popleft()
    for next_node in graph[cur_node] :
        if indegree[next_node] > 0 :
            indegree[next_node] -= 1
            if indegree[next_node] == 0 :
                visited.append(next_node)
                q.append(next_node)

print(visited)
print(len(visited) == numCourses)