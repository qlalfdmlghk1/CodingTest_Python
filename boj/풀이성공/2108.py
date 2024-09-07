n = int(input())
numbers = []
for i in range(n) :
    numbers.append(int(input()))
dic = {}

# 1. 평균값
first = int(round(sum(numbers)/n,0))

# 2. 중앙값
numbers.sort()
second = numbers[n//2]

# 3. 최빈값
for i in numbers :
    if i in dic :
        dic[i] += 1
    else :
        dic[i] = 1
numbers_dic = sorted(dic.items(), key=lambda items: items[1],reverse=True)
if n > 1 :
    if numbers_dic[0][1] == numbers_dic[1][1] :
        third = numbers_dic[1][0]
    else :
        third = numbers_dic[0][0]
else:
    third = numbers[0]
fourth = numbers[n-1] - numbers[0]
print(first)
print(second)
print(third)
print(fourth)
