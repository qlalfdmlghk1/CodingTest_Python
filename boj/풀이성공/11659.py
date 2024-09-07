import sys
input = sys.stdin.readline
n,m = map(int, input().split())
arr = list(map(int, input().split()))
new_arr = []
sum = 0
for i in arr :
    sum += i
    new_arr.append(sum)

for _ in range(m) :
    start, end = map(int, input().split())
    if start == 1 :
        print(new_arr[end-1])
    else :
        print(new_arr[end-1] - new_arr[start - 2])