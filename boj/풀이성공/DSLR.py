from collections import deque
t = int(input())

for _ in range(t) :
    q = deque()
    a,b = map(int,input().split())
    q.append((a,''))
    while q :
        cur, commend = q.popleft()
        if cur == b :
            print(commend)
            break

        cur_d = (cur * 2) % 10000
        commend_d = commend + 'D'
        q.append((cur_d, commend_d))

        if cur == 0 :
            cur_s = 9999
        else :
            cur_s = cur - 1
        commend_s = commend + 'S'
        q.append((cur_s, commend_s))

        cur_l = (cur % 1000) * 10 + (cur // 1000)
        commend_l = commend + 'L'
        q.append((cur_l, commend_l))

        cur_r = (cur // 10) + (cur % 10) * 1000
        commend_r = commend + 'R'
        q.append((cur_r, commend_r))



