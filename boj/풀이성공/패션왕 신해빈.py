from collections import defaultdict
t = int(input())

for _ in range(t) :
    sum = 1
    n = int(input())
    dic = defaultdict(list)
    for i in range(n) :
        item, kinds = map(str, input().split())
        dic[kinds].append(item)
    for j in dic.values() :
        sum *= (len(j) + 1)
    print(sum-1)