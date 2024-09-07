n = int(input())
arr = list(map(int,input().split()))
dic_nums = {}
answer = []
arr2 = set(arr)
arr2 = sorted(arr2)

for i, num in enumerate(arr2) :
    if num not in dic_nums :
        dic_nums[num] = i

for num in arr :
    answer.append(str(dic_nums[num]))

print(' '.join(answer))