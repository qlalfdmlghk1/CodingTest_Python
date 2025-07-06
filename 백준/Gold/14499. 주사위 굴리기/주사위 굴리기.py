# 지도의 세로 크기 N, 가로 크기 M (1 ≤ N, M ≤ 20), 주사위를 놓은 곳의 좌표 x, y, 명령의 개수 K
n,m,x,y,k = map(int,input().split())
graph = []
for _ in range(n) :
    graph.append(list(map(int,input().split())))

# 이동하는 명령 : 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4 (4 4 4 1 3 3 3 2)
command = list(map(int,input().split()))

dice = [0,0,0,0,0,0]

def turn(dir) :
    a,b,c,d,e,f = dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] # 임시 저장
    if dir == 1 : # 동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d,b,a,f,e,c
    elif dir == 2 : # 서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c,b,f,a,e,d
    elif dir == 3 : # 북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e,a,c,d,f,b
    elif dir == 4 : # 남
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b,f,c,d,a,e

dr = [0,0,0,-1,1]
dc = [0,1,-1,0,0]

for i in command :
    nex_r = x + dr[i]
    nex_c = y + dc[i]
    if 0 <= nex_r < n and 0 <= nex_c < m :
        turn(i)
        if graph[nex_r][nex_c] == 0 :
            graph[nex_r][nex_c] = dice[5]
        else :
            dice[5] = graph[nex_r][nex_c]
            graph[nex_r][nex_c] = 0
        x, y = nex_r, nex_c
        print(dice[0])