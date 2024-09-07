n = int(input())
tri = []
dp = []
for i in range(n) :
    arr = list(map(int,input().split()))
    tri.append(arr)
    dp.append(arr)

for i in range(1,n) :
    for j in range(len(tri[i])) :
        if j == 0 :
            dp[i][j] = dp[i-1][j] + tri[i][j]
        elif j == i :
            dp[i][j] = dp[i-1][j-1] + tri[i][j]
        else :
            dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + tri[i][j]
print(max(tri[n-1]))