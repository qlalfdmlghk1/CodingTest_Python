import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1) :
    u,v,r = map(int,input().split())
    graph[u].append((v,r))
    graph[v].append((u,r))

def bfs(start) :
    q = deque()
    visited = [-1] * (n+1)
    visited[start] = 0
    q.append((start,visited[start]))
    while q :
        cur_node,distance = q.popleft()
        for next_node,next_distance in graph[cur_node] :
            if visited[next_node] == -1 :
                visited[next_node] = visited[cur_node] + next_distance
                q.append((next_node,visited[next_node]))
    return(visited.index(max(visited)))

def bfs_tree(start) :
    q = deque()
    visited = [-1] * (n+1)
    visited[start] = 0
    q.append((start,visited[start]))
    while q :
        cur_node,distance = q.popleft()
        for next_node,next_distance in graph[cur_node] :
            if visited[next_node] == -1 :
                visited[next_node] = visited[cur_node] + next_distance
                q.append((next_node,visited[next_node]))
    print(max(visited))


bfs_tree(bfs(1))