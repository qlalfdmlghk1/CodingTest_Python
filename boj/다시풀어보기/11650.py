import sys
input = sys.stdin.readline
n,m = map(int, input().split())
graph = []
dp = []

for _ in range(n) :
    graph.append(list(map(int, input().split())))

for i in range(1,n+1) :
    for j in range(1,m+1) :
        dp[i][j] = dp[i][j-1] + dp[i-1][j] + dp[i-1][j-1]