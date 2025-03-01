from collections import deque

# (r,c)로부터 맨해튼 거리 2 이하로 앉아있는 'P'가 있으면 False 반환.
# (r,c)로부터 거리유지가 다 잘되고 있으면 True 반환
def bfs(r, c, place):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    visited = [[False] * 5 for _ in range(5)]
    q = deque()
    q.append((r, c, 0))
    visited[r][c] = True
    while q:
        cur_r, cur_c, cur_dist = q.popleft()
        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            next_dist = cur_dist + 1
            if 0 <= next_r < 5 and 0 <= next_c < 5 and place[next_r][next_c] != "X" :
                if visited[next_r][next_c] == False :
                # next distance가 2 이하를 넘어서면 건너뛴다.
                    if next_dist > 2:
                        continue
                    # next distance가 2 이하면서 값이 'P'면 False반환. 거리두기 실패
                    if place[next_r][next_c] == "P":
                        return False

                    q.append((next_r, next_c, next_dist))
                    visited[next_r][next_c] = True
    return True


def check(place):
    # place 안에 있는 모든 'P'에 대해서 거리두기가 잘 되고 있는지 확인
    for r in range(5):
        for c in range(5):
            if place[r][c] == "P":
                # bfs가 False를 반환하면 이번 place는 거리두기 실패!
                if bfs(r, c, place) == False :
                    return False
    return True


def solution(places):
    answer = []
    for i in places:
        # 거리두기 잘 지켜지는지 확인하는 함수 => True를 반환하면 1 추가
        if check(i):
            answer.append(1)
        # 거리두기 잘 지켜지는지 확인하는 함수 => False를 반환하면 0 추가
        else:
            answer.append(0)
    return answer