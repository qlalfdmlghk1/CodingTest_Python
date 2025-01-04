# 좋은 문제다 (dp의 정석)
def solution(m, n, puddles):
    dp = [[0 for i in range(m)] for i in range(n)]
    pud = {}
    for x,y in puddles :
        pud[(y-1,x-1)] = True

    for i in range(n) :
        for j in range(m) :
            # print(i,j)
            # print(dp)
            if (i,j) in pud :
                continue
            else :
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0 :
                    dp[i][j] = dp[i][j-1]
                elif j == 0 :
                    dp[i][j] = dp[i-1][j]
                else :
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

    answer = dp[n-1][m-1] % 1000000007
    return answer