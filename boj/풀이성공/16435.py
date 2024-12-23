n,length = map(int,input().split())  # 과일 수, 처음 길이
fruits = list(map(int,input().split()))
fruits.sort()

for fruit in fruits :
    if length >= fruit :
        length += 1
    else :
        break
print(length)

