def findSet(parents, a) :
    if parents[a] != a :
        parents[a] = findSet(parents,parents[a])
    return parents[a]

def union(parents,a,b) :
    aRoot = findSet(parents,a)
    bRoot = findSet(parents,b)
    if aRoot < bRoot :
        parents[bRoot] = aRoot
    elif bRoot < aRoot :
        parents[aRoot] = bRoot

n = int(input())
parents = [0] * (n+1)
xList = []
yList = []
edges = []
result = 0
arr = list(i for i in range(n))

from itertools import combinations

for _ in range(n) :
    x,y = map(float, input().split())
    xList.append(x)
    yList.append(y)

for i in range(n) :
    parents[i] = i

for i in range(n-1) :
    for j in range(i+1,n) :
        cost = round(((xList[i] - xList[j])**2 + (yList[i] - yList[j])**2)**0.5, 2)
        edges.append((cost,i,j))
edges.sort()

for edge in edges :
    if findSet(parents,edge[2]) != findSet(parents,edge[1]) :
        union(parents,edge[1],edge[2])
        result += edge[0]

print(result)


