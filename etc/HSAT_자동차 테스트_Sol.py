import bisect
import sys
input = sys.stdin.readline

n,q = map(int, input().strip().split())
cars = list(map(int, input().strip().split()))
cars.sort()  # 이분탐색은 정렬이 되어 있어야 함
setCars = set(cars)  # 탐색 시간 줄이기 위해 set으로 바꿈 -> 안하면 시간초과 발생 O(1)

for _ in range(q) :
    targetValue = int(input())
    if targetValue not in setCars :
        print(0)
    else :
        idx = bisect.bisect_left(cars,targetValue)  # bisect_left : 리스트에서 주어진 값이 삽입될 수 있는 가장 왼쪽 인덱스를 반환
        print(idx * (n - idx - 1))  # targetValue의 인덱스 기준으로 왼쪽 중 1개, 오른쪽 중 1개를 선택하면 됨