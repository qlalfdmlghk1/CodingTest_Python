import sys
input = sys.stdin.readline

while True :
    try :
        x = int(input())
        x *= 10000000
        n = int(input())
        lego = []
        answer = "danger"
        for _ in range(n) :
            lego.append(int(input()))
        lego.sort()

        left = 0
        right = n-1
        while left < right :
            if lego[left] + lego[right] == x :
                answer = "yes" + " " + str(lego[left]) + " " + str(lego[right])
                break
            elif lego[left] + lego[right] < x :
                left += 1
            else :
                right -= 1
        print(answer)
    except :
        exit()