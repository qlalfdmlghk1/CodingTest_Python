from itertools import combinations
number = input()
k = int(input())
cnt = 0
stack = []

for idx,n in enumerate(number) :
    while stack and cnt < k and stack[-1] < n :
        stack.pop()
        cnt += 1
    stack.append(n)

    if cnt >= k:
        for j in range(idx + 1, len(number)):
            stack.append(number[j])
        break

print(''.join(stack[0:len(number)-k]))

