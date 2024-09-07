nums = [100,4,200,1,3,2]

dic = {}
answer = 0

for num in nums :
    dic[num] = True

for i in nums :
    if i-1 not in dic :
        cnt = 1
        target = i + 1
        while target in dic :
            target += 1
            cnt += 1
        answer = max(cnt,answer)
print(answer)