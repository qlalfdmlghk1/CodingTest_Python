n = int(input())
arr = list(map(int,input().split()))
dp1 = [0] * n
dp2 = [0] * n
for idx in range(1,n) :
    for idx2 in range(0,idx) :
        if arr[idx] > arr[idx2] :
            dp1[idx] = max(dp1[idx2] + 1, dp1[idx])
        if arr[n-1-idx] > arr[n-idx+idx2] :
            dp2[n-1-idx] = max(dp2[n-idx+idx2] + 1, dp2[n-1-idx])

answer = 0
for i in range(n) :
    answer = max(dp1[i] + dp2[i], answer)
print(answer + 1)
