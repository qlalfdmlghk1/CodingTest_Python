def solution(k, d):
    answer = 0
    for i in range(0,d+1,k) :
        max_y = (d**2 - i**2)**(1/2)
        # if max_y % k == 0 :
        answer += int(max_y // k) + 1
        # else :
        #     answer += int(max_y // k)
    return answer