from collections import deque

def bfs(r, c) :
    answer = -1
    row_len, col_len = len(grid), len(grid[0])
    visited = [[0] * col_len for _ in range(row_len)]

    queue = deque()
    queue.append((r,c))
    visited[r][c] = 1
    dr = [1, 1, 1, -1, -1, -1, 0, 0]
    dc = [-1, 0, 1, -1, 0, 1, 1, -1]

    while queue :
        cur_r, cur_c = queue.popleft()
        print(queue)
        for i in range(8) :
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0 <= next_r < row_len and 0 <= next_c < col_len :
                if grid[next_r][next_c] == 0 and visited[next_r][next_c] == 0 :
                    visited[next_r][next_c] = visited[cur_r][cur_c] + 1
                    queue.append((next_r,next_c))
                    # print(next_r,next_c)
                    # print(row_len - 1, col_len - 1)
                    if next_r == row_len - 1 and next_c == col_len - 1:
                        print(visited[row_len - 1][col_len - 1])
                        break



grid = [[0,0,0],[1,1,0],[1,1,0]]
bfs(0,0)

# for i in range(row_len) :
#     for j in range(col_len) :
#         if grid[i][j] == 0 :
#             bfs(i,j)

