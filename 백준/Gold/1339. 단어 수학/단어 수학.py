n = int(input())
words = []
alpha = []

for i in range(26) :
    alpha.append([i,0])    

for _ in range(n) :
    s = input()
    words.append(s)

for word in words :
    for idx,w in enumerate(word) :
        alpha[ord(w)-65][1] += 10**(len(word)-idx-1)

alpha.sort(key = lambda x : x[1], reverse=True)

num = 9
answer = 0
for a in alpha :
    if a[1] != 0 :
        answer += (num * a[1])
    num -= 1
print(answer)