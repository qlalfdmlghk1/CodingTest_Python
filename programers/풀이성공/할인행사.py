want,number	= ["apple"],[10]
discount = ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]
from collections import Counter
n = len(discount)
dic_items = {}
wanted_dict = {}
wanted = []
answer = 0

for i,j in zip(want,number) :
    for _ in range(j) :
        wanted.append(i)
wanted_dict = Counter(wanted)

for i in range(n-9) :
    if wanted_dict == Counter(discount[i:i+10]) :
        answer += 1
print(answer)
