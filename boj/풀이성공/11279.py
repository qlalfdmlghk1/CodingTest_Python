from heapq import heapify, heappush, heappop
n = int(input())
hq = []
for _ in range(n) :
    num = int(input())
    if num == 0 :
        if len(hq) != 0 :
            print(-1 * heappop(hq))
        else :
            print(0)
    else :
        heappush(hq,-1 * num)