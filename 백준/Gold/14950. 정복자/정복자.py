
n,m,t = map(int, input().split())  # 도시 수, 도로 수, 도로 비용


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

parents = [0] * (n+1)
edges = []
result = 0

for i in range(1,n+1) :
    parents[i] = i

for _ in range(m) :
    a,b,cost = map(int,input().split())
    edges.append((a,b,cost))
edges.sort(key = lambda x : x[2])

if len(edges) == 1 : result -= t

cnt = 0  # 몇 개의 간선을 선택했는지 카운트
for edge in edges:
    a, b, cost = edge
    if findSet(parents, a) != findSet(parents, b):
        union(parents, a, b)
        result += cost + (cnt * t)
        cnt += 1

print(result)