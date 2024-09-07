# 사전에 알파벳 모음 'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는, 길이 5 이하의 모든 단어가 수록되어 있다.
# 사전에서 첫 번째 단어는 "A"이고, 그다음은 "AA"이며, 마지막 단어는 "UUUUU"입니다.
# 단어 하나 word가 매개변수로 주어질 때, 이 단어가 사전에서 몇 번째 단어인지 return.
word = "EIO"
from itertools import product
alpha = ['A', 'E', 'I', 'O', 'U']
answer = []

for i in range(1,6) :
    for j in product(alpha, repeat = i) :
        sum = ''.join(j)
        answer.append(sum)

answer.sort()

for index,w in enumerate(answer) :
    if word == w :
        print(index + 1)