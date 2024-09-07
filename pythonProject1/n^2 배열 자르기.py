n,left,right = 3,2,5	# result = [3,2,2,3]
answer = []
for i in range(left,right+1) :
    answer.append(max(i//n,i%n)+1)
print(answer)