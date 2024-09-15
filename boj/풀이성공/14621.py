import sys
input = sys.stdin.readline
n,m = map(int, input().split())  # 학교의 수, 도로의 수
university = list(map(str, input().split()))
parents = [0] * (n+1)
edges = []
result = 0

for _ in range(m) :
    u,v,d = map(int, input().split())
    if university[u-1] != university[v-1] :
        edges.append((d, u, v))
edges.sort()

for i in range(n+1) :
    parents[i] = i

def findSet(parents,a) :
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

for edge in edges :
    cost,a,b = edge
    if findSet(parents,a) != findSet(parents,b) :
        union(parents,a,b)
        result += cost

for i in range(1,n+1) :
    if parents[parents[i]] != parents[1] :
        result = -1
        break
print(result)