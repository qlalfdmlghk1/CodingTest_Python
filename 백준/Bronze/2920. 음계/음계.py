# ascending, descending, mixed

music = list(map(int,input().split()))

if music[0] == 1 :
    answer = "ascending"
    for i in range(1,8) :
        if music[i] < music[i-1] :
            answer = "mixed"
            break
elif  music[0] == 8 :
    answer = "descending"
    for i in range(1,8) :
        if music[i] > music[i-1] :
            answer = "mixed"
            break
else :
    answer = "mixed"
print(answer)