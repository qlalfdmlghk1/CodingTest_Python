n = int(input())
buildings = list(map(int, input().split()))
answer = 0

for i in range(n) :
    cnt = 0
    standard_l = float('INF')
    standard_r = -1 * float('INF')
    print(standard_r)

    for left in range(i-1,-1,-1) :
        slope = (buildings[i] - buildings[left]) / (i - left)
        if slope < standard_l:
            standard_l = slope
            cnt += 1
        # print((buildings[i] - buildings[left]) / (i - left))

    for right in range(i+1,n) :
        slope = (buildings[right] - buildings[i]) / (right - i)
        if slope > standard_r:
            standard_r = slope
            cnt += 1

    answer = max(answer,cnt)

print(answer)

# n = int(input())
# buildings = list(map(int, input().split()))
# answer = 0
#
# for i in range(n):
#     cnt = 0
#     max_slope_left_num = None
#     max_slope_left_den = None
#     max_slope_right_num = None
#     max_slope_right_den = None
#
#     # 왼쪽 빌딩 확인
#     for left in range(i - 1, -1, -1):
#         dy = buildings[left] - buildings[i]
#         dx = left - i  # 음수 값이지만 부호를 맞춰줌
#         if max_slope_left_num is None:
#             max_slope_left_num = dy
#             max_slope_left_den = dx
#             cnt += 1
#         else:
#             # 기울기 비교: 현재 기울기가 최대 기울기보다 큰지 확인
#             if dy * max_slope_left_den > max_slope_left_num * dx:
#                 max_slope_left_num = dy
#                 max_slope_left_den = dx
#                 cnt += 1
#
#     # 오른쪽 빌딩 확인
#     for right in range(i + 1, n):
#         dy = buildings[right] - buildings[i]
#         dx = right - i
#         if max_slope_right_num is None:
#             max_slope_right_num = dy
#             max_slope_right_den = dx
#             cnt += 1
#         else:
#             # 기울기 비교: 현재 기울기가 최대 기울기보다 작은지 확인
#             if dy * max_slope_right_den < max_slope_right_num * dx:
#                 max_slope_right_num = dy
#                 max_slope_right_den = dx
#                 cnt += 1
#
#     answer = max(answer, cnt)
#
# print(answer)
