def solution(players,m,k):
    answer = 0
    servers = [1 for _ in range(24)]
    for i in range(24) :
        while players[i] >= servers[i] * m :
            for j in range(k) :
                if i+j < 24 :
                    servers[i+j] += 1
            answer += 1
    return answer