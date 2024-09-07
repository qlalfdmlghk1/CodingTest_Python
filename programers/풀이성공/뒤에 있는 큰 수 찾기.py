
# 시간초과 코드
'''
answer = []
arr2 = []

for index,num in enumerate(numbers) :
    for index2,num2 in enumerate(numbers[index+1:]) :
        if num < num2 :
            answer.append(num2)
            break
        elif index2 == len(numbers[index+1:]) - 1 :
            answer.append(-1)

answer.append(-1)
print(answer)'''
numbers	= [9, 1, 5, 3, 6, 2]
#result = [-1, 5, 6, 6, -1, -1]

answer = [-1] * len(numbers)
stack = []
for i in range(len(numbers)) :
    while stack and numbers[stack[-1]] < numbers[i] :
        answer[stack.pop()] = numbers[i]
    stack.append(i)
print(answer)
