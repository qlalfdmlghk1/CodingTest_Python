from collections import deque
rooms = [[1],[2],[3],[]]
visited = [False] * len(rooms)
q = deque()
def dfs(start):
    visited[start] = True
    for next_node in rooms[start] :
        if visited[next_node] == False :
            visited[next_node] = True
            dfs(next_node)

def bfs(start) :
    q.append(start)
    visited[start] = True
    while q :
        next_node = q.popleft()
        for next in rooms[next_node] :
            if visited[next] == False:
                visited[next] = True
                q.append(next)

# dfs(0)
bfs(0)
print(visited)
if False in visited :
    print(False)
else :
    print(True)

