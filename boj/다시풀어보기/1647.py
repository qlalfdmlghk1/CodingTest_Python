n,m = map(int,input().split())
houses = [[] for _ in range(n+1)]
visited = [[False] for _ in range(n+1)]

def findSet(parents,a) :
    if parents[a] != a :
        parents[a] = findSet(parents, parents[a])
    return parents[a]

def union(parents,a,b) :
    aRoot = findSet(parents,a)
    bRoot = findSet(parents,b)
    if aRoot < bRoot :
        parents[bRoot] = aRoot
    else :
        parents[aRoot] = bRoot

parents = [0] * (n+1)
edges = []
result = 0

for i in range(1,n+1) :
    parents[i] = i

for _ in range(m) :
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))
    edges.append((cost,b,a))
edges.sort()

for edge in edges :
    cost,a,b = edge
    if findSet(parents,a) != findSet(parents,b) :
        union(parents,a,b)
        result += cost
        last_edge = cost
print(result - last_edge)

    