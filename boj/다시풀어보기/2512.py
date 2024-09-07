n = int(input())
money = list(map(int, input().split()))
m = int(input())

result = 0  # 출력할 최대 예산
start, end = 1, max(money)

while start <= end :
    mid = (start + end) // 2  # 설정할 상한값
    total = 0  # 예산의 합
    for i in money :
        if i > mid :        # 상한값보다 요청된 예산이 크다면
            total += mid    # 상한값 배정
        else :              # 상한값보다 요청된 예산이 작다면
            total += i      # 예산 모두 배정

    if total <= m :      # 계산한 값이 예산 총액보다 작다면
        result = mid
        start = mid + 1  # 시작값을 mid+1 로 변경
    else :               # 계산한 값이 예산 총액보다 크다면
        end = mid - 1    # 종료값을 mid-1로 변경
print(result)