import sys
input = sys.stdin.readline
# 풀이1)
# for house in color_money :
#     if ind != house.index(min(house)) :
#         min_pay += min(house)
#         ind = house.index(min(house))
#         print(min(house))
#     else :
#         house[house.index(min(house))] +=1000
#         min_pay += min(house)
#         ind = house.index(min(house))
#         print(min(house))
# print(min_pay)


# 풀이2
# from collections import deque
# q = deque()
# n = int(input())
# color_money = []
# for _ in range(n) :
#     color_money.append(list(map(int,input().split())))
#
# total = []
#
# q.append((0,color_money[0][0],color_money[0][0]))
# q.append((0,color_money[0][1],color_money[0][1]))
# q.append((0,color_money[0][2],color_money[0][2]))
#
# while q :
#     ind,money,min_pay = q.popleft()
#     ind += 1
#     if ind >= n:
#         total.append(min_pay)
#     else :
#         for i in range(3) :
#             if i != color_money[ind-1].index(money) :
#                 q.append((ind, color_money[ind][i], min_pay+color_money[ind][i]))
#
# print(min(total))


# 해설 기반 풀이)
n = int(input())
houses = []
for _ in range(n) :
    houses.append(list(map(int,input().split())))

for i in range(1,n) :
    houses[i][0] = min(houses[i-1][1], houses[i-1][2]) + houses[i][0]
    houses[i][1] = min(houses[i-1][0], houses[i-1][2]) + houses[i][1]
    houses[i][2] = min(houses[i-1][0], houses[i-1][1]) + houses[i][2]
print(min(houses[n-1]))