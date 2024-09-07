n,lost,reserve	 = 5,[2, 4],[1, 3, 5]
# return = 5
lost_final = list(set(lost) - set(reserve))
reserve_final = list(set(reserve) - set(lost))


cnt = 0
for i in lost_final :
    if (i - 1) in reserve_final :
        reserve_final.pop(reserve_final.index(i-1))
    elif (i + 1) in reserve_final :
        reserve_final.pop(reserve_final.index(i+1))
    else :
         cnt += 1
print(n - cnt)