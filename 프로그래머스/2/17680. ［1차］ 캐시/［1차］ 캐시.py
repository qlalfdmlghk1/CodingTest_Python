# 이미 큐에 들어가 있는 상태에서 호출되었을 때, 그 cite를 가장 최근에 호출되었다고 어떻게 표현하나
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


def solution2(cacheSize, cities):
    stack = []
    answer = 0
    for i in cities :
        if len(stack) >= cacheSize :
            if i.upper() in stack :
                stack.append(stack.pop(stack.index(i.upper())))
                answer += 1
            else :
                stack.append(i.upper())
                stack.pop(0)
                answer += 5
        else :
            if i.upper() in stack :
                stack.append(stack.pop(stack.index(i.upper())))
                answer += 1
            else :
                stack.append(i.upper())
                answer += 5
    return answer
    
    


from collections import deque
def solution3(cacheSize, cities):
    q = []
    answer = 0
    k = 0
    for i in range(len(cities)) :
        for index_j, j in enumerate(q) :
            if j == i :
                q.append(j.upper())
                q.pop(index_j)
            answer += 5
        if len(q) == 3 :
            k = i
            break
            
    for i in cities[k+1:] :
        for index_j, j in enumerate(q) :
            if j == i :
                q.append(j.upper())
                q.pop(index_j)
        else :
            answer += 5
            q.append(i.upper())
            q.pop(0)
    return answer



from collections import deque
def solution4(cacheSize, cities):
    answer = 0
    q = deque(cacheSize)

    for city in cities:
        city = city.lower()     # 대소문자 구분 없이 처리하기 위해 소문자로 변환
        if city in q:       
            answer += 1         # 실행 시간 1 증가
            q.remove(city)  # 캐시에서 해당 도시를 제거
            q.append(city)  # 캐시의 맨 끝에 도시를 다시 삽입
        else:  # 캐시 미스
            answer += 5         # 실행 시간 5 증가
            q.append(city)  # 새 도시를 캐시에 삽입

    return answer