#  ‘I n’은 정수 n을 Q에 삽입하는 연산을 의미한다. 동일한 정수가 삽입될 수 있음을 참고하기 바란다.
#  ‘D 1’는 Q에서 최댓값을 삭제하는 연산을 의미하며, ‘D -1’는 Q 에서 최솟값을 삭제하는 연산을 의미한다.
#  최댓값(최솟값)을 삭제하는 연산에서 최댓값(최솟값)이 둘 이상인 경우, 하나만 삭제됨을 유념하기 바란다.
#
# 만약 Q가 비어있는데 적용할 연산이 ‘D’라면 이 연산은 무시해도 좋다. Q에 저장될 모든 정수는 -231 이상 231 미만인 정수이다.
#
# 출력은 표준출력을 사용한다. 각 테스트 데이터에 대해, 모든 연산을 처리한 후 Q에 남아 있는 값 중 최댓값과 최솟값을 출력하라.
#  두 값은 한 줄에 출력하되 하나의 공백으로 구분하라. 만약 Q가 비어있다면 ‘EMPTY’를 출력하라.

import sys
input = sys.stdin.readline
from heapq import heapify,heappop,heappush
t = int(input())
for _ in range(t) :
    min_hq = []
    max_hq = []
    n = int(input())
    visited = [False] * n
    for i in range(n) :
        # print(min_hq)
        # print(max_hq)
        a,b = input().split()
        if a == 'I' :
            heappush(min_hq,(int(b),i))
            heappush(max_hq, (-1 * int(b),i))
        elif a == 'D' :
            # print(visited)
            if b == '1' :
                while max_hq and visited[max_hq[0][1]] :
                    heappop(max_hq)
                if max_hq :
                    visited[max_hq[0][1]] = True
                    heappop(max_hq)

            elif b == '-1' :
                while min_hq and visited[min_hq[0][1]]:
                    heappop(min_hq)
                if min_hq:
                    visited[min_hq[0][1]] = True
                    heappop(min_hq)

    # print(min_hq)
    # print(max_hq)
    # print(visited)

    while max_hq and visited[max_hq[0][1]] :
        heappop(max_hq)
        # print(max_hq)
    while min_hq and visited[min_hq[0][1]] :
        heappop(min_hq)
        # print(min_hq)

    if min_hq and max_hq:
        print(-1 * max_hq[0][0], min_hq[0][0])
    else :
        print('EMPTY')
