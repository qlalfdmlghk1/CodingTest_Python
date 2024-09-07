# 왜 오류가 생길까?
from collections import deque

t = int(input())
for i in range(t):
    order = input()
    n = int(input())
    arr = input()[1:-1].split(',')
    q = deque(arr)

    rev = 0

    for j in order:
        if len(q) == 0:
            break
        if j == 'R':
            rev += 1
        elif j == 'D':
            if rev % 2 == 0:
                q.popleft()
            else:
                q.pop()

    if len(q) == 0:
        print("error")
    elif rev % 2 == 1:
        q.reverse()
        print("["+",".join(q)+"]")
    elif rev % 2 == 0:
        print("["+",".join(q)+"]")