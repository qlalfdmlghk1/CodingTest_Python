import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t) :
    m = int(input())
    size = m // 10 + 1
    arr = []
    new_arr = []
    print(m//2 + 1)
    cnt = 0
    while size > 0 :
        lists = list(map(int,input().split()))
        for i in lists :
            arr.append(i)
        size -= 1

    for i in range(m) :
        new_arr.append(arr[i])
        if (i % 2 == 0) :
            if i == 0 :
                print(new_arr[0], end = ' ')
                cnt += 1
            else :
                new_arr.sort()
                cnt += 1
                print(new_arr[len(new_arr) // 2], end = ' ')
            if cnt > 9 :
                cnt = 0
                print()
    print()


# import sys, heapq
# input = sys.stdin.readline
#
# t = int(input())
# for _ in range(t):
#     m = int(input())
#     arr = list(map(int, input().split()))
#     print(m // 2 + 1)
#
#     low = []      # 최대 힙
#     high = []     # 최소 힙
#     result = []
#
#     for i in range(m) :
#         if len(low) == len(high) :
#             heapq.heappush(low, -arr[i])  # 최대 힙
#         else :
#             heapq.heappush(high, arr[i])  # 최소 힙
#
#         if high and -low[0] > high[0] :  # 최대 힙의 루트가 최소 힙의 루트보다 큰 경우
#
#             # 최대 힙의 루트(최대 값)과 최소 힙의 루트(최소 값)를 비교
#             # 만약 최대 힙의 루트 값이 최소 힙의 루트 값보다 크면 두 값을 교환
#             max_low = -heapq.heappop(low)  # 최대 힙에서 가장 큰 값을 꺼내기 (음수로 저장되어 있으므로 다시 양수로 변환)
#             min_high = heapq.heappop(high)  # 최소 힙에서 가장 작은 값을 꺼내기
#
#             # 꺼낸 값을 서로 교환하여 최대 힙과 최소 힙의 특성을 유지
#             heapq.heappush(low, -min_high)  # 최소 힙의 작은 값을 최대 힙에 음수로 다시 넣음
#             heapq.heappush(high, max_low)  # 최대 힙에서 꺼낸 큰 값을 최소 힙에 다시 넣음
#
#         if i % 2 == 0:  # 짝수 번째마다 중간 값을 출력
#             result.append(-low[0])
#
#         for i in range(len(result)):
#             if i > 0 and i % 10 == 0:
#                 print()
#             print(result[i], end=' ')
#         print()