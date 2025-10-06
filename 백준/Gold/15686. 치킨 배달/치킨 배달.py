import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque

n,m = map(int, input().split())
graph = []
for _ in range(n) :
    graph.append(list(map(int,input().split())))

chickens = []
houses = []
cnt = 0
for i in range(n) :
    for j in range(n):
        if graph[i][j] == 2 :
            chickens.append((i,j))
        if graph[i][j] == 1 :
            houses.append((i,j))

answer = 1e6
for chick in combinations(chickens,m) :
    sum = 0
    for house in houses :
        dis = int(1e6)
        for c in chick :
            dis = min(dis,abs(c[0]-house[0])+abs(c[1]-house[1]))
        sum += dis
    answer = min(answer,sum)

print(answer)
