# 해설ver 파이참에 있다.
# 어느 정도 그냥 암기할 필요도 있다고 생각.
def solution(n):
    answer = []
    def hanoi(n,start,end,mid) :
        if n == 1 :
            answer.append([start,end])
            return
        else :
            hanoi(n-1, start,mid,end)
            answer.append([start,end])
            hanoi(n-1, mid,end,start)


    hanoi(n,1,3,2)
    return answer