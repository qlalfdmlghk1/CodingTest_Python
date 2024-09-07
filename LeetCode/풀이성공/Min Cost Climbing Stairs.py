cost = [1,100,1,1,1,100,1,1,100,1]
n = len(cost)
dp = {}
dp[0] = 0
dp[1] = 0
for index in range(2,n+1) :
    dp[index] = min(dp[index-1] + cost[index-1], dp[index-2] + cost[index-2])
print(dp[n])