import sys
input = sys.stdin.readline
#
# def dfs(r, c, idx, total):
#     global ans
#     if ans >= total + max_val * (3 - idx):
#         return
#     if idx == 3:
#         ans = max(ans, total)
#         return
#     else:
#         for i in range(4):
#             nex_r = r + dr[i]
#             nex_c = c + dc[i]
#             if 0 <= nex_r < n and 0 <= nex_c < m and visit[nex_r][nex_c] == 0:
#                 if idx == 1:
#                     visit[nex_r][nex_c] = 1
#                     dfs(r, c, idx + 1, total + graph[nex_r][nex_c])
#                     visit[nex_r][nex_c] = 0
#                 visit[nex_r][nex_c] = 1
#                 dfs(nex_r, nex_c, idx + 1, total + graph[nex_r][nex_c])
#                 visit[nex_r][nex_c] = 0
#
#
# n, m = map(int, input().split())
# graph = []
# for _ in range(n) :
#     graph.append(list(map(int, input().split())))
# # graph = [list(map(int, input().split())) for _ in range(n)]
# visit = [[0 for _ in range(m)]  for _ in range(n)]
#
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]
# ans = 0
# max_val = max(map(max, graph))
#
# for r in range(n):
#     for c in range(m):
#         visit[r][c] = 1
#         dfs(r, c, 0, graph[r][c])
#         visit[r][c] = 0
#
# print(ans)

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

n,m = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# 최대값 변수
maxValue = 0

# ㅗ, ㅜ, ㅓ, ㅏ 제외한 모양들 최대값 계산
def dfs(r, c, dsum, cnt):
    global maxValue
    # 모양 완성되었을 때 최대값 계산
    if cnt == 4:
        maxValue = max(maxValue, dsum)
        return

    # 상, 하, 좌, 우로 이동
    for i in range(4):
        nex_r = r + dr[i]
        nex_c = c + dc[i]
        if 0 <= nex_r < n and 0 <= nex_c < m and not visited[nex_r][nex_c]:
            # 방문 표시 및 제거
            visited[nex_r][nex_c] = True
            dfs(nex_r, nex_c, dsum + board[nex_r][nex_c], cnt+1)
            visited[nex_r][nex_c] = False

from itertools import combinations
# ㅗ, ㅜ, ㅓ, ㅏ 모양의 최대값 계산
def exce(r, c):
    global maxValue
    arr = [0,1,2,3]
    tmp = board[r][c]
    # move 배열의 요소를 3개씩 사용할 수 있도록 인덱스 계산
    for k in combinations(arr,3):   # 012, 123, 230, 301
        for i in range(3) :
            nex_r = r + dr[k[i]]
            nex_c = c + dc[k[i]]

            if not (0 <= nex_r < n and 0 <= nex_c < m):
                tmp = 0
                break
            tmp += board[nex_r][nex_c]
    # 최대값 계산
        maxValue = max(maxValue, tmp)
        tmp = 0


for i in range(n):
    for j in range(m):
        # 시작점 visited 표시
        visited[i][j] = True
        dfs(i, j, board[i][j], 1)
        visited[i][j] = False

        exce(i, j)

print(maxValue)