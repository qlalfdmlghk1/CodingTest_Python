n = int(input())
num = [i for i in range(n+2)]
answer = 1

def dfs(x) :
    global answer
    if x > n :
        return
    answer *= num[x]
    dfs(x+1)

dfs(1)
print(answer)