while True :
    try :
        n = int(input())
        number = ''
        while True :
             number += '1'
             if int(number) % n == 0 :
                 print(len(number))
                 break
    except :
        exit()