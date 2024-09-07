import sys
input = sys.stdin.readline
k,n = map(int, input().split())
lens = []
for _ in range(k) :
    lens.append(int(input()))
lens.sort()
start = 0
end = lens[-1]
while start <= end :
    result = 0
    mid = (start + end) // 2
    for j in lens:
        result += (j//mid)
    if result < n :
        end = mid - 1
    elif result >= n :
        start = mid + 1
print(end)



# lens.sort()
# mini = lens[0]
# maxi = lens[-1]
# for i in range(maxi,0,-1) :
#     result = 0
#     for j in lens :
#         result += (j//i)
#     if result == n :
#         print(i)
#         break
