a,b = map(str, input().split())
aList = []
bList = []

def changeNum(x,list) :
    x1 = x
    x1 = x1.replace("5","6")
    list.append(int(x1))

    x2 = x
    x2 = x2.replace("6", "5")
    list.append(int(x2))

changeNum(a, aList)
changeNum(b, bList)
aList.sort()
bList.sort()

print(aList[0]+bList[0], aList[1]+bList[1])



