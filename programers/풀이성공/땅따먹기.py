land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
n = len(land)
m = len(land[0])
for i in range(1,n) :
    for j in range(m) :
        if j == 0 :
            land[i][j] = max(land[i-1][1],land[i-1][2],land[i-1][3]) + land[i][j]
        elif j == 1:
            land[i][j] = max(land[i-1][0], land[i-1][2], land[i-1][3]) + land[i][j]
        elif j == 2 :
            land[i][j] = max(land[i - 1][1], land[i - 1][0], land[i - 1][3]) + land[i][j]
        elif j == 3:
            land[i][j] = max(land[i - 1][1], land[i - 1][2], land[i - 1][0]) + land[i][j]
print(max(land[n-1]))