# 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다
# 0층의 i호에는 i명이 산다
# k층에 n호에는 몇 명이 살고 있는지 출력
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t) :
    k = int(input())
    n = int(input())
    dp = [[0 for _ in range(n)] for _ in range(k+1)]
    dp[0] = [i for i in range(1,n+1)]
    for j in range(1,k+1) :
        for m in range(n) :
            dp[j][m] = dp[j-1][m] + dp[j][m-1]
    print(dp[k][n-1])