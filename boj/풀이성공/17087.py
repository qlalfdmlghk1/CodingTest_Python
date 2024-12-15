import math
import sys
input = sys.stdin.readline

n,s = map(int, input().split())  # n : 동생 수, s : 현재 위치
brothers = list(map(int, input().split()))
distance = []

for b in brothers :
    distance.append(abs(b-s))

x = distance[0]
for d in distance[1:] :
    x = math.gcd(x,d)
print(x)

