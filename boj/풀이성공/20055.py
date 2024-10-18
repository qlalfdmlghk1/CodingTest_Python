import sys
input = sys.stdin.readline
from collections import deque
n,k = map(int, input().split())
belt = deque(list(map(int, input().split())))  # 내구도
robat = deque([0] * n)  # 로봇 개수

answer = 0

while True :
    answer += 1

    # 순서 1번
    belt.rotate(1)
    robat.rotate(1)
    robat[n-1] = 0  # 내리는 위치에 도달하면 로봇 내림

    # 순서 2번
    for i in range(n-2, -1, -1) :
        if robat[i] >= 1 and robat[i+1] == 0 and belt[i+1] >= 1 : # 이동하려는 칸에 로봇이 없고, 내구성 남아있으면
            robat[i+1] = 1  # 옮긴 칸 -> 로봇 : 1
            robat[i] = 0    # 옮기기 전 칸 -> 로봇 : 0
            belt[i+1] -= 1  # 로봇 이동 -> 내구도 -1

    robat[n-1] = 0

    # 순서 3번
    if belt[0] != 0 :
        robat[0] = 1
        belt[0] -= 1


    # 순서 4번
    if belt.count(0) >= k :
        break

print(answer)
