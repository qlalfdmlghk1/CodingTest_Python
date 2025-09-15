from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course :
        candidate = []
        for order in orders :
            for i in combinations(order,c) :
                menu = ''.join(i)
                print(menu)
                menu = sorted(menu)
                candidate.append(''.join(menu))
        sorted_menu = Counter(candidate).most_common()

        for sm in sorted_menu :
            if sm[1] >= 2 and sm[1] == sorted_menu[0][1] :
                answer.append(sm[0])

    answer.sort()
    return answer