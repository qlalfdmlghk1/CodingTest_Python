import sys
input = sys.stdin.readline

c1 = list(map(int,input().strip()))
c2 = list(map(int,input().strip()))
c3 = list(map(int,input().strip()))
c4 = list(map(int,input().strip()))

k = int(input())

for _ in range(k) :
    direction = [0, 0, 0, 0, 0]
    num, dir = map(int, input().split())
    direction[num] = dir

    # 1번 톱니바퀴라면
    if num == 1 :
        if c1[2] != c2[6] :
            direction[2] = (direction[1] * -1)
        if c2[2] != c3[6] :
            direction[3] = (direction[2] * -1)
        if c3[2] != c4[6] :
            direction[4] = (direction[3] * -1)

    # 2번 톱니바퀴라면
    if num == 2 :
        if c1[2] != c2[6] :
            direction[1] = (direction[2] * -1)
        if c2[2] != c3[6] :
            direction[3] = (direction[2] * -1)
        if c3[2] != c4[6] :
            direction[4] = (direction[3] * -1)

    # 3번 톱니바퀴라면
    if num == 3 :
        if c3[2] != c4[6] :
            direction[4] = (direction[3] * -1)
        if c2[2] != c3[6] :
            direction[2] = (direction[3] * -1)
        if c1[2] != c2[6] :
            direction[1] = (direction[2] * -1)

    # 4번 톱니바퀴라면
    if num == 4 :
        if c3[2] != c4[6] :
            direction[3] = (direction[4] * -1)
        if c2[2] != c3[6] :
            direction[2] = (direction[3] * -1)
        if c1[2] != c2[6] :
            direction[1] = (direction[2] * -1)

    if direction[1] == 1 :
        c1.insert(0,c1.pop())
    elif direction[1] == -1 :
        c1.append(c1.pop(0))

    if direction[2] == 1 :
        c2.insert(0,c2.pop())
    elif direction[2] == -1 :
        c2.append(c2.pop(0))

    if direction[3] == 1 :
        c3.insert(0,c3.pop())
    elif direction[3] == -1 :
        c3.append(c3.pop(0))

    if direction[4] == 1 :
        c4.insert(0,c4.pop())
    elif direction[4] == -1 :
        c4.append(c4.pop(0))

answer = c1[0] + (c2[0] * 2) + (c3[0] * 4) + (c4[0] * 8)
print(answer)