def solution(today, terms, privacies):
    answer = []
    dic = {}
    todays = [int(today[0:4]), int(today[5:7]),int(today[8:10])]

    for term in terms :
        a,b = term.split()
        dic[a] = int(b)

    for index,privacie in enumerate(privacies) :
        end = []
        day,al = privacie.split()
        if al in dic :
            month = int(privacie[5:7]) + dic[al]
            year = int(privacie[0:4])
        while month > 12 :
            month -= 12
            year += 1
        end = [year, month, int(privacie[8:10])]


        if end[0] < todays[0] :
            answer.append(index+1)
        elif end[0] == todays[0] :
            if end[1] < todays[1] :
                answer.append(index+1)
            elif end[1] == todays[1] :
                if end[2] <= todays[2] :
                    answer.append(index+1)

    return answer