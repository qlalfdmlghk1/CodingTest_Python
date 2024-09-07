import math
arr	= [1,2,3]
while len(arr) >= 2 :
    arr.append(math.lcm(arr.pop(),arr.pop()))
print(arr[0])