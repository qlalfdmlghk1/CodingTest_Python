t = int(input())

for _ in range(t) :
    dic = {}
    n = int(input())
    note1 = list(map(int,input().split()))
    m = int(input())
    note2 = list(map(int, input().split()))
    for i in note1 :
        dic[i] = True

    for j in note2 :
        if j in dic :
            print(1)
        else :
            print(0)