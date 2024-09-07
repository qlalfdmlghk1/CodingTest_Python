# 첫째 줄에 유저의 수 N (2 ≤ N ≤ 100)과 친구 관계의 수 M (1 ≤ M ≤ 5,000)이 주어진다.
# 둘째 줄부터 M개의 줄에는 친구 관계가 주어진다.
# 친구 관계는 A와 B로 이루어져 있으며, A와 B가 친구라는 뜻이다.
# A와 B가 친구이면, B와 A도 친구이며, A와 B가 같은 경우는 없다.
# 친구 관계는 중복되어 들어올 수도 있으며, 친구가 한 명도 없는 사람은 없다.
# 또, 모든 사람은 친구 관계로 연결되어져 있다. 사람의 번호는 1부터 N까지이며, 두 사람이 같은 번호를 갖는 경우는 없다.
#
# 첫째 줄에 BOJ의 유저 중에서 케빈 베이컨의 수가 가장 작은 사람을 출력한다.
# 그런 사람이 여러 명일 경우에는 번호가 가장 작은 사람을 출력한다.
from collections import deque
n,m = map(int,input().split())
graph = [[0] for i in range(n+1)]

for i in range(m) :
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

q = deque()
def bfs(k) :
    visited = [0] * (n + 1)
    q.append(k)
    while q :
        cur = q.popleft()
        for next_v in graph[cur] :
            if visited[next_v] == 0 :
                visited[next_v] = visited[cur] + 1
                q.append(next_v)
    visited[0] = 0
    visited[k] = 0
    # print(visited)
    return sum(visited)


answer = []
for i in range(1,n+1) :
    tar = bfs(i)
    answer.append(tar)

mini = min(answer)
for index, friend in enumerate(answer) :
    if mini == friend :
        print(index+1)
        break