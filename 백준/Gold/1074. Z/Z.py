import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())  # n: 몇 승, r: 행, c: 열

def z(n, r, c):
    result = 0
    size = 2 ** n  # 전체 크기 (한 변의 길이)
    
    while size > 1:
        size //= 2  # 4개의 영역으로 나누기 위한 크기 조정
        if r < size and c < size:  # 1사분면 (좌상단)
            pass  # 변화 없음
        elif r < size and c >= size:  # 2사분면 (우상단)
            result += size * size
            c -= size  # 현재 위치를 2사분면의 좌상단 기준으로 이동
        elif r >= size and c < size:  # 3사분면 (좌하단)
            result += size * size * 2
            r -= size  # 현재 위치를 3사분면의 좌상단 기준으로 이동
        else:  # 4사분면 (우하단)
            result += size * size * 3
            r -= size
            c -= size

    print(result)

z(n, r, c)
