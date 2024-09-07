nums = [3,3]
target = 6
answer = []

dic = {}
for index,num in enumerate(nums) :
    if num in dic :
        answer.append(dic[num])
        answer.append(index)
    else :
        dic[target-num] = index
    # print(dic)
print(answer)