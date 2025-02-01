n = int(input())

for _ in range(n) :
    st = input()
    score = 1
    answer = 0
    stack = []
    for s in st :
        if s == 'O' :
            if stack and stack[-1] == 'O' :
                score += 1
            else :
                score = 1
        else :
            score = 0
        stack.append(s)
        answer += score 
    print(answer)
            