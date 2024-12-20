n = int(input())
charge = 1000 - n
changes = [500,100,50,10,5,1]
cnt = 0
for ch in changes :
    cnt += (charge // ch)
    charge = charge % ch
print(cnt)
# n = int(input())
# charge = 1000 - n
# cnt,cnt1,cnt2,cnt3,cnt4,cnt5 = 0,0,0,0,0,0
# while True :
#     while charge // 500 >= 1 :
#         cnt1 = charge // 500
#         charge -= (cnt1*500)
#     while charge // 100 >= 1 :
#         cnt2 = charge // 100
#         charge -= (cnt2 * 100)
#     while charge // 50 >= 1 :
#         cnt3 = charge // 50
#         charge -= (cnt3 * 50)
#     while charge // 10 >= 1 :
#         cnt4 = charge // 10
#         charge -= (cnt4 * 10)
#     while charge // 5 >= 1 :
#         cnt5 = charge // 5
#         charge -= (cnt5 * 5)
#     cnt += charge
#     break
# # print(cnt1,cnt2,cnt3,cnt4,cnt5)
# cnt += cnt1
# cnt += cnt2
# cnt += cnt3
# cnt += cnt4
# cnt += cnt5
# print(cnt)