text1 = "abcba"
text2 = "abcbcba"
answer = []
list1 = []

for i in text1 :
    list1.append(i)

for i in list1 :
    for index,j in enumerate(text2) :
        if i == j :
            answer.append(index)
n = len(answer)
dp = [1] * n
for i in range(n) :
    for j in range(i) :
        if answer[j] < answer[i] :
            dp[i] = max(dp[i], dp[j] + 1)
print(dp)
print(max(dp))
