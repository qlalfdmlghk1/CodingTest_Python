import sys
input = sys.stdin.readline
from itertools import combinations

n,q = map(int, input().strip().split())
cars = list(map(int, input().strip().split()))

def middleValueCheck(targetValue) :
    global cnt
    for car in combinations(cars,3) :
        car = list(car)
        car.sort()
        if car[1] == targetValue :
            cnt += 1
    print(cnt)

for _ in range(q) :
    cnt = 0
    targetValue = int(input().strip())
    middleValueCheck(targetValue)

