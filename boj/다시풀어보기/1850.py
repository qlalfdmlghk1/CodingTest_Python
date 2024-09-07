import math

A,B = map(int, input().split())
A = int('1' * A)
B = int('1' * B)
gcd = math.gcd(A, B)
print(gcd)