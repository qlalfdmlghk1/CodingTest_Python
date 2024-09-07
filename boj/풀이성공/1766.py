import sys, heapq
input = sys.stdin.readline
n,m = map(int, input().split())  # 문제 수, 먼저 푸는게 좋은
indegree = [0] * (n+1)           # 들어오는 간선 수 저장
pre = [[] for _ in range(n+1)]   # 선행 노드 저장
answer = []

for _ in range(m) :
    a,b = map(int, input().split())
    indegree[b] += 1
    pre[a].append(b)

pq = []  # 우선 순위 큐

for cur in range(1,n+1) :
    if indegree[cur] == 0 :
        heapq.heappush(pq,cur)  # heapq.heappush -> 작은 노드일수록 가장 앞으로 정렬

while pq :
    cur = heapq.heappop(pq)
    answer.append(cur)
    for nex in pre[cur] :
        indegree[nex] -= 1
        if indegree[nex] == 0 :
            heapq.heappush(pq, nex)

print(*answer)