n = int(input())
graph = []
for _ in range(n) :
    graph.append(list(map(int,input().split())))
blue, gray = 0,0
def paper_cutting(r,c,n) :
    global blue, gray
    standard_color = graph[r][c]
    for i in range(r,r+n):
        for j in range(c,c+n):
            if graph[i][j] != standard_color :
                paper_cutting(r, c, n//2)
                paper_cutting(r+n//2, c, n//2)
                paper_cutting(r, c+n//2, n//2)
                paper_cutting(r+n//2, c+n//2, n//2)
                return   # 없으면 처음 저장해놓은 숫자와 달라도 반복문이 끝나면 색종이 개수가 카운트
    else :
        if standard_color == 1 :
            blue += 1
        else :
            gray += 1

paper_cutting(0,0,n)
print(blue)
print(gray)
