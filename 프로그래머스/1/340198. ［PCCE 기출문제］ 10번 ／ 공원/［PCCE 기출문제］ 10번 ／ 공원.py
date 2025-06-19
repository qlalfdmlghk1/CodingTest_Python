def solution(mats, park):
    n,m = len(park),len(park[0])
    dp_park = [[] for _ in range(n)]
    for i in range(n) :
        for j in range(m) :
            if park[i][j] == "-1" :
                dp_park[i].append(1)
            else :
                dp_park[i].append(0)

    max_length = 0

    for i in range(n) :
        for j in range(m) :
            if dp_park[i][j] == 1 :
                if i == 0 or j == 0 :
                    continue
                else :
                    if dp_park[i-1][j-1] != 0 and dp_park[i][j-1] != 0 and dp_park[i-1][j] != 0 :
                        dp_park[i][j] = min(dp_park[i-1][j-1], dp_park[i][j-1], dp_park[i-1][j]) + 1

            max_length = max(max_length,dp_park[i][j])
    #         print(max_length)
    # print(dp_park)

    for dp in dp_park :
        max_length = max(max_length,max(dp))

    mats.sort(reverse=True)
    for mat in mats :
        if mat <= max_length :
            return mat
    return -1