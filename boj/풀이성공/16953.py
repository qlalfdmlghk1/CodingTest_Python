import sys
input = sys.stdin.readline
from collections import deque

a,b = map(int,input().split())
q = deque()
q.append((a,1))

def check_answer(nex_num,nex_cnt) :
    global b
    if nex_num == b:
        print(nex_cnt)
        exit()

while q :
    cur_num,cur_cnt = q.popleft()
    for i in range(2) :
        if i == 0 :
            nex_num = cur_num * 2
            if nex_num <= b :
                nex_cnt = cur_cnt + 1
                q.append((nex_num,nex_cnt))
                check_answer (nex_num,nex_cnt)
        else :
            nex_num = int(str(cur_num) + "1")
            if nex_num <= b:
                nex_cnt = cur_cnt + 1
                q.append((nex_num,nex_cnt))
                check_answer (nex_num,nex_cnt)

print(-1)

# if visited[b] == 1 :
#     print(-1)
# else :
#     print(visited[b])


# sys.setrecursionlimit(10 ** 9)
#
# def dfs(start, cnt) :
#     cur = start
#     if cur == b :
#         return cnt
#     for i in range(2):
#         if i == 0 :
#             nex = cur * 2
#             dfs(nex,cnt+1)
#         else :
#             nex = int(str(cur) + "1")
#             dfs(nex, cnt + 1)
# print(dfs(a,1))