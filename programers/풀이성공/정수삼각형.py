def solution(triangle):
    dp = triangle
    for i in range(1,len(triangle)) :
        for j in range(i+1) :
            if j == 0 :
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif i == j :
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else :
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + triangle[i][j], dp[i-1][j] + triangle[i][j])
    return max(dp[-1])