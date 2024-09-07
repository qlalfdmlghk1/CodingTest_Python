s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
answer = []
dic = {}
s = s.replace('{','')
s = s.replace('}','')
s = s.replace(',',' ')
arr = list(map(int, s.split()))
for i in arr :
    if i in dic :
        dic[i] += 1
    else :
        dic[i] = 1
dic = sorted(dic.items(), key = lambda item : item[1], reverse = True)
# print(dic)
for i in dic :
    answer.append(int(i[0]))
print(answer)