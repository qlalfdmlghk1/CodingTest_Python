import sys
sys.setrecursionlimit(100000)
v,e = map(int,input().split())

parents = [0] * (v+1)
for i in range(1,v+1) :
    parents[i] = i

edges = []
for _ in range(e) :
    a,b,c = map(int,input().split())
    edges.append((a,b,c))
edges.sort(key=lambda x:x[2])

def findSet(parents,a) :
    if parents[a] != a :
        parents[a] = findSet(parents,parents[a])
    return parents[a]

def union(parents,a,b) :
    aRoot = findSet(parents,a)
    bRoot = findSet(parents,b)
    if aRoot < bRoot :
        parents[bRoot] = aRoot
    else :
        parents[aRoot] = bRoot

result = 0
for edge in edges :
    a,b,c = edge
    if findSet(parents,a) != findSet(parents,b) :
        union(parents,a,b)
        result += c
print(result)