def solution(ingredient):
    answer = 0
    stack = []
    for ingre in ingredient :
        stack.append(ingre)
        if ingre == 1 and len(stack) >= 4 :  # 1이면 앞의 4개 확인
            if stack[-4:] == [1, 2, 3, 1] :
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                answer += 1

    return answer