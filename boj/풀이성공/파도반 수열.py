# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9

dp = [0] * 100001
dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
dp[6] = 3

t = int(input())
for _ in range(t) :
    n = int(input())
    if n >= 7 :
        for i in range(7,n+1) :
            dp[i] = dp[i-2] + dp[i-3]
    print(dp[n])