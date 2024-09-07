import sys
input = sys.stdin.readline
n = int(input())
people = []
for idx in range(n) :
    person = list(map(int,input().split()))
    people.append(person)
-
for i in people :
    rank = 1
    for j in people :
        if i[0] < j[0] and i[1] < j[1] :
            rank += 1
    print(rank, end=' ')