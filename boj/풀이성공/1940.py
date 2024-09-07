n = int(input())
m = int(input())
array = list(map(int,input().split()))

lp,rp = 0,n-1
cnt = 0

array.sort()

while (lp < rp) :
    if (array[lp] + array[rp] == m ) :
        cnt += 1
        lp += 1
        rp -= 1
    elif (array[lp] + array[rp] < m ) :
        lp += 1
    else :
        rp -= 1
print(cnt)