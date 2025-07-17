def solution(n, times):
    answer = 0
    left, right = 0,max(times) * n
    while left <= right :
        mid = (left + right) // 2
        people = 0
        for time in times :
            people += mid // time
            if people > n : # 시간이 너무 적다는 것
                break
        if people >= n : # 시간이 너무 적다는 것
            answer = mid
            right = mid - 1
        else : # 시간이 너무 길다
            left = mid + 1
    return answer