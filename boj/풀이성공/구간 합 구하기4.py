import sys
input = sys.stdin.readline
m,n = map(int, input().split())
numbers = list(map(int, input().split()))
sum_arr = [0]
sum = 0

for i in numbers :
    sum += i
    sum_arr.append(sum)

for i in range(n) :
    start,end = map(int, input().split())
    print(sum_arr[end] - sum_arr[start-1])