dic = {"black" : 0, "brown":1, "red":2, "orange":3, "yellow":4, "green":5, "blue":6, "violet":7, "grey":8, "white":9}

a = input()
b = input()
c = input()

num = str(dic[a]) + str(dic[b])
print(int(num) * 10 ** dic[c])