# 네 개의 정수 M, N, x와 y가 주어질 때, <M:N>이 카잉 달력의 마지막 해라고 하면 <x:y>는 몇 번째 해를 나타내는지.
import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t) :
    cnt = 1
    cur_x, cur_y = 1, 1
    m, n, x, y = map(int, input().split())
    while cur_x != x or cur_y != y :
        cur_x += 1
        cur_y += 1
        cnt += 1
        if cnt > m * n :
            cnt = -1
            print(-1)
            break
        if cur_x == x and cur_y == y :
            print(cnt)
            break
        else :
            if cur_x > m :
                cur_x = 1
            if cur_y > n :
                cur_y = 1