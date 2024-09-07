n,left,right = 4,7,14	# result = [3,2,2,3]

#24.05.03
answer = []
for i in range(left,right+1) :
    a = i // n
    b = i % n
    answer.append((max(a,b))+1)
print(answer)

# 24.05.03
# answer = []
# graph = [[n for _ in range(n)]for _ in range(n)]
# for i in range(n) :
#     for j in range(n) :
#         graph[i][j] = max(i+1,j+1)
# for i in range(n) :
#     for k in graph[i] :
#         answer.append(k)
# print(answer[left:right+1])

# sol 24.01.01
# for i in range(left,right+1) :
#     answer.append(max(i//n,i%n)+1)
# print(answer)