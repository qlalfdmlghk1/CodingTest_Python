G = int(input())

answer = []

left = 1
right = 2

while left < right :
    weight = right ** 2 - left ** 2
    # print(weight)
    # if weight > 100000 :
    #     break
    if weight > G :
        left += 1
    elif weight < G :
        right += 1
    elif weight == G :
        answer.append(right)
        left += 1

if not answer :
    print(-1)
else :
    for i in answer :
        print(i)
