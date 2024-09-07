# 특정 원소가 속한 집합을 찾는 함수
def findSet(parents,a) :
    if parents[a] != a :
        parents[a] = findSet(parents,parents[a])
    return parents[a]

# 두 원소가 속한 집합 합치는 함수
def union(parents,a,b) :
    aRoot = findSet(parents, a)
    bRoot = findSet(parents, b)
    if a < b:
        parents[bRoot] = aRoot
    else:
        parents[aRoot] = bRoot


# Main
v, e = map(int, input().split())  # 노드, 간선 수
parents = [0] * (v + 1)
edges = []    # 간선 정보 담을 리스트
result = 0    # 최소 신장 트리 계산 변수

# 자기 자신을 부모로 초기화
for i in range(1, v+1) :
    parents[i] = i

# 간선을 입력받아 cost를 기준으로 오름차순
for _ in range(e) :
    a,b,cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

# 정렬된 간선을 하나씩 확인
for edge in edges :
    cost, a, b = edge
    # 두 노드의 루트 노드가 서로 다르다면 사이클이 발생하지 않은 것
    if findSet(parents,a) != findSet(parents,b) :
        # 신장 트리에 간선 추가
        union(parents,a,b)
        result += cost

print(result)