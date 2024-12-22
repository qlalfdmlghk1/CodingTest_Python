t = int(input())
minutes = [300,60,10]
answer = []

if t % 10 != 0 :
    print(-1)
else :
    for minu in minutes :
        answer.append(str(t // minu))
        t %= minu

    print(' '.join(answer))