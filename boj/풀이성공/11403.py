from collections import deque
q = deque()
n = int(input())
board = []
graph = [[] for _ in range(n)]
new_graph = [['0' for _ in range(n)] for _ in range(n)]
visited = [False] * n

for _ in range(n) :
    board.append(list(map(int,input().split())))

for i in range(n) :
    for j in range(n) :
        if board[i][j] == 1 :
            graph[i].append(j)

def bfs(v) :
    arr = []
    q.append(v)
    while q :
        cur = q.popleft()
        arr.append(cur)
        for nex in graph[cur] :
            if visited[nex] == False :
                q.append(nex)
                visited[nex] = True
    for i in range(len(arr)-1) :
        for j in range(i+1, len(arr)):
            new_graph[arr[0]][arr[j]] = '1'

for i in range(n) :
    bfs(i)
    visited = [False] * n

for i in range(n) :
    print(' '.join(new_graph[i]))