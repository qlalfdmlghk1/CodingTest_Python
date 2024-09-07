# from collections import deque
# n = int(input())
# graph = []
#
#
# for i in range(n) :
#     graph.append(list(map(int,input().split())))
#
# def bfs(y,x,direction,cnt) :
#     cur_r = y
#     cur_c = x
#
#     if direction == 1 :
#         dr1 = [0, 1]
#         dc1 = [1, 1]
#         for i in range(2) :
#             nr = cur_r + dr1[i]
#             nc = cur_c + dc1[i]
#             if (nr == n - 1) and (nc == n - 1):
#                 cnt += 1
#                 print(f"도달! : {cur_r}, {cur_c} => {nr}, {nc}")
#                 return
#             if (0 <= nr < n and 0 <= nc < n and graph[nr][nc] == 0):
#                 print(f"{cur_r}, {cur_c} => {nr}, {nc}")
#                 bfs(nr,nc,1,cnt)
#     elif direction == 2 :
#         dr2 = [1, 1]
#         dc2 = [0, 1]
#         for i in range(2) :
#             nr = cur_r + dr2[i]
#             nc = cur_c + dc2[i]
#             if (nr == n - 1) and (nc == n - 1):
#                 cnt += 1
#                 print(f"도달! : {cur_r}, {cur_c} => {nr}, {nc}")
#                 return
#             if (0 <= nr < n and 0 <= nc < n and graph[nr][nc] == 0):
#                 print(f"{cur_r}, {cur_c} => {nr}, {nc}")
#                 bfs(nr, nc, 2, cnt)
#     elif direction == 3 :
#         dr3 = [0, 1, 1]
#         dc3 = [1, 0, 1]
#         for i in range(3) :
#             nr = cur_r + dr3[i]
#             nc = cur_c + dc3[i]
#             if (nr == n - 1) and (nc == n - 1):
#                 cnt += 1
#                 print(f"도달! : {cur_r}, {cur_c} => {nr}, {nc}")
#                 return
#             if (0 <= nr < n and 0 <= nc < n and graph[nr][nc] == 0) :
#                 print(f"{cur_r}, {cur_c} => {nr}, {nc}")
#                 bfs(nr,nc,3,cnt)
#     return cnt
#
#
# re1 = bfs(0, 1, 1, 0)
#
# print(re1)


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# dp 배열 초기화 (3차원 배열, 0: 가로, 1: 대각선, 2: 세로)
dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]

def pipe():
    # dp 배열 초기화
    dp[0][0][1] = 1  # 가로 방향으로 시작

    # 1행 처리
    for i in range(2, n):
        if board[0][i] == 0:  # 벽이 없으면
            dp[0][0][i] = dp[0][0][i - 1]  # 가로 방향으로 계속 이어짐

    # 나머지 셀 처리
    for r in range(1, n):
        for c in range(1, n):
            if board[r][c] == 0:  # 현재 셀이 벽이 아니면

                # 대각선 파이프를 추가
                if board[r][c - 1] == 0 and board[r - 1][c] == 0:
                    dp[1][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]

                # 가로 파이프를 추가
                if c - 1 >= 0:
                    dp[0][r][c] = dp[0][r][c - 1] + dp[1][r][c - 1]

                # 세로 파이프를 추가
                if r - 1 >= 0:
                    dp[2][r][c] = dp[2][r - 1][c] + dp[1][r - 1][c]

    print(sum(dp[i][n - 1][n - 1] for i in range(3)))

pipe()

