n = int(input())
m = int(input())
s = input()

p = 'I' +'OI' * n
cnt = 0

for i in range(m-len(p)) :
    if s[i:i+len(p)] == p :
        cnt += 1
print(cnt)