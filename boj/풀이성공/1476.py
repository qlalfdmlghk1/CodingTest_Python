import sys
input = sys.stdin.readline

E,S,M = map(int, input().split())
# 1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19

for year in range(1,int(1e9)) :
    if (year - E)%15 == 0 and (year - S)%28 == 0 and (year - M)%19 == 0 :
        print(year)
        break