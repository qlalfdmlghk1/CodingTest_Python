matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
m = len(matrix)
n = len(matrix[0])
maxlen = 0
dp = [[0 for i in range(n+1)] for j in range(n+1)]

for i in range(m) :
    for j in range(n) :
        if matrix[i][j] == '1' :
            dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1], dp[i][j]) + 1
            maxlen = max(maxlen, dp[i+1][j+1])
print(maxlen*maxlen)