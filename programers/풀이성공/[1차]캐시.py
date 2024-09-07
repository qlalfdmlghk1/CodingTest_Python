def solution(cacheSize, cities):
    q = []
    answer = 0
    for i in cities :
        if i.upper() in q :
                q.pop(q.index(i.upper()))
                q.append(i.upper())
                answer += 1
        else :
            answer += 5
            q.append(i.upper())
            if len(q) > cacheSize :
                q.pop(0)
    return answer