strs = ["eat","tea","tan","ate","nat","bat"]
answer = []
from collections import defaultdict
dic = defaultdict(list)
for word in strs :
    dic[''.join(sorted(word))].append(word)

for i in dic.values() :
    answer.append(i)
print(answer)
