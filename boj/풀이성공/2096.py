n = int(input())
dp_max = []
dp_min = [[] for _ in range(n)]

for i in range(n) :
    k = list(map(int,input().split()))
    dp_max.append(k)
    dp_min.append(k)
for i in range(n) :
    for j in dp_max[i] :
        dp_min[i].append(j)


for i in range(n-2,-1,-1) :
    for j in range(3) :
        if j == 0 :
            dp_min[i][j] = min(dp_min[i+1][j], dp_min[i+1][j+1]) + dp_min[i][j]
            dp_max[i][j] = max(dp_max[i+1][j], dp_max[i+1][j+1]) + dp_max[i][j]
        elif j == 1 :
            dp_min[i][j] = min(dp_min[i+1][j], dp_min[i+1][j+1], dp_min[i+1][j-1]) + dp_min[i][j]
            dp_max[i][j] = max(dp_max[i+1][j], dp_max[i+1][j+1], dp_max[i+1][j-1]) + dp_max[i][j]
        elif j == 2:
            dp_min[i][j] = min(dp_min[i+1][j-1], dp_min[i+1][j]) + dp_min[i][j]
            dp_max[i][j] = max(dp_max[i+1][j-1], dp_max[i+1][j]) + dp_max[i][j]
print(max(dp_max[0]),min(dp_min[0]),end=' ')