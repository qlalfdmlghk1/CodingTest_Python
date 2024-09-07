T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    answer = 0
    n = int(input())
    buildings = list(map(int,input().split()))
    for i in range(2,n-1) :
        if buildings[i] < buildings[i-1] or buildings[i] < buildings[i-2] or buildings[i] < buildings[i+1] or buildings[i] < buildings[i+2] :
            continue
        else :
            result = buildings[i] - max(buildings[i-1],buildings[i-2],buildings[i+1],buildings[i+2])
        answer += result
    print(f"#{test_case} {answer}")
