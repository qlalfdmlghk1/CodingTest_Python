import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque
n,m = map(int,input().split())
k = list(map(int,input().split()))
graph = [[] for _ in range(n+1)]
parties = []
for _ in range(m) :
    arr = list(map(int,input().split()))
    for i in combinations(arr[1:],2) :
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    parties.append(arr[1:])

q = deque()
dic = {}
for i in k[1:] :
    q.append(i)
    dic[i] = True
    while q :
        cur = q.popleft()
        for node in graph[cur] :
            if node not in dic :
                dic[node] = True
                q.append(node)
cnt = 0

for party in parties :
    for i in party :
        if i in dic :
            break
    else :
        cnt += 1
print(cnt)