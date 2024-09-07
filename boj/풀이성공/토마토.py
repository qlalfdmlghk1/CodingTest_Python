# import sys
# input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
q = deque()
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))

while q:
    cur_r, cur_c = q.popleft()
    for i in range(4):
        next_r = cur_r + dr[i]
        next_c = cur_c + dc[i]
        if 0 <= next_r < n and 0 <= next_c < m and graph[next_r][next_c] == 0:
            graph[next_r][next_c] = graph[cur_r][cur_c] + 1
            q.append((next_r, next_c))

for i in range(n):
    if 0 in graph[i] :
        answer = 0
        break
    answer = max(answer,max(graph[i]))

print(answer-1)