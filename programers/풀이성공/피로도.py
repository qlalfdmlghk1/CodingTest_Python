from itertools import permutations
def solution(k, dungeons):
    dungeons.sort(key = lambda x : (x[1],x[0]))
    n = len(dungeons)
    answer = 0
    for h in permutations(dungeons,n) :
        cnt = 0
        hp = k
        for i,j in h :
            if hp >= i :
                hp -= j
                cnt += 1
        answer = max(cnt,answer)
    return answer