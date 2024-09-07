from collections import deque

numCourses = 2
prerequisites = []
answer = []

graph = [[] for _ in range(numCourses)]
indegree = [0] * numCourses
for u,v in prerequisites :
    graph[v].append(u)
    indegree[u] += 1

q = deque()
for i,pre in enumerate(indegree) :
    if pre == 0 :
        q.append(i)
        answer.append(i)

while q :
    cur = q.popleft()
    for next_course in graph[cur] :
        indegree[next_course] -= 1
        if indegree[next_course] == 0 :
            answer.append(next_course)
            q.append(next_course)

if len(answer) == numCourses :
    print(answer)
else :
    print([])

