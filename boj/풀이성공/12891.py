import sys
input = sys.stdin.readline

s, p = map(int, input().split())
dna = input()
arr = list(map(int, input().split()))
lp, rp, cnt = 0, p-1, 0

password = dna[lp:rp]
for j in password:
    if j == 'A': arr[0] -= 1
    elif j == 'C': arr[1] -= 1
    elif j == 'G': arr[2] -= 1
    elif j == 'T': arr[3] -= 1


while rp <= s-1 :
    if dna[rp] == 'A': arr[0] -= 1
    elif dna[rp] == 'C': arr[1] -= 1
    elif dna[rp] == 'G': arr[2] -= 1
    elif dna[rp] == 'T': arr[3] -= 1

    cnt += 1
    for j in arr :
        if j > 0 :
            cnt -= 1
            break

    if dna[lp] == 'A': arr[0] += 1
    elif dna[lp] == 'C': arr[1] += 1
    elif dna[lp] == 'G': arr[2] += 1
    elif dna[lp] == 'T': arr[3] += 1

    lp += 1
    rp += 1

print(cnt)