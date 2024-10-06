# import sys
# input = sys.stdin.readline
# k,n = map(int, input().split())
# lens = []
# for _ in range(k) :
#     lens.append(int(input()))
# lens.sort()
# start = 0
# end = lens[-1]
# while start <= end :
#     result = 0
#     mid = (start + end) // 2
#     for j in lens:
#         result += (j//mid)
#     if result < n :
#         end = mid - 1
#     elif result >= n :
#         start = mid + 1
# print(end)


import sys
input = sys.stdin.readline
k,n = map(int, input().split())
lines = []
for _ in range(k) :
    lines.append(int(input()))
start = 0
mid = 0
end = max(lines)

while start <= end :
    mid = (start + end) // 2
    cnt = 0
    for line in lines :
        cnt += (line // mid)

    if cnt >= n :
        start = mid + 1
    elif cnt < n :
        end = mid - 1

print(mid)
# while True:
#     cnt = 0
#     mid += 1
#     for line in lines :
#         cnt += (line // mid)
#         if cnt != n :
#             print(mid-1)
#             exit()