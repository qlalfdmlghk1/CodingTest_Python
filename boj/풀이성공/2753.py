year = int(input())

# 윤년 : 4의 배수 && 100의 배수가 아닐 때 || 400의 배수

if year % 400 == 0 :
    answer = 1
elif year % 100 == 0 :
    answer = 0
elif year % 4 == 0 :
    answer = 1
else :
    answer = 0
print(answer)