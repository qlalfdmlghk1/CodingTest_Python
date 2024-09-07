m, n = 3, 2
dp = [[0 for i in range(n)] for i in range(m)]
dp[0][0] = 0
dp[1][0] = 1
dp[0][1] = 1
for i in range(0,m) :
    for j in range(0,n) :
        if i == 0 or j == 0 :
            dp[i][j] = 1
        else :
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[m-1][n-1])
