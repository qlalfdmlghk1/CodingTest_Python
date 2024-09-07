n = int(input())
# 스택 2개 만들어서 이동 할 것임
numbers = []
stack = []
answer = []
for i in range(n,0,-1) :
    numbers.append(i)   # numbers = [8,7,6,5,4,3,2,1] -> 오름 차순으로 빼려면 이렇게 저장해 둬야 함.

for _ in range(n) :
    k = int(input())
    while numbers and numbers[-1] <= k :
        stack.append(numbers.pop())        # k 숫자까지 stack에 넣었다가
        answer.append('+')
    if stack[-1] == k :
        answer.append('-')
        stack.pop()                        # stack에서 k 숫자 pop
        continue    # for _ in range(n) 문으로 이동
    # 주어진 수열 만들 수 없다면
    else :
        answer = ["NO"]
        break

for i in answer :
    print(i)