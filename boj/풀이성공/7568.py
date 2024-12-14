n = int(input())
people = []
for i in range(n) :
    people.append(list(map(int,input().split())))
    people[i].append(i+1)
people.sort(reverse=True)

rank = 1

for i in range(n) :
    rank = 1
    if i == 0 :
        people[i].append(rank)
    else :
        for j in range(i) :
            if people[j][0] > people[i][0] and people[j][1] > people[i][1] :
                rank += 1
        people[i].append(rank)

people.sort(key = lambda x : x[2])

for p in people :
    print(p[3],end=" ")