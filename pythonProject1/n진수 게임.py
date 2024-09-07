# n : 진법, t : 미리 구할 숫자의 갯수, m : 게임에 참가하는 인원, p : 튜브의 순서
n,t,m,p	= 16,	16,	2,	2
# n	t	m	p	result
# 2	4	2	1	"0111"
# 16	16	2	1	"02468ACE11111111"
# 16	16	2	2	"13579BDF01234567"
def check(num) :
    game = ''
    arrange = '0123456789ABCDEF'
    if num == 0 :
        return '0'
    while num > 0 :
        a,b = divmod(num,n)
        num //= n
        game += arrange[b]
    return game[::-1]

answer = ''
result = ''
c = p - 1

for i in range(t*m+1) :
    answer += check(i)
    # print(answer)
while len(result) < t :
    result += answer[c]
    c += m
    # print(result)
print(result)

