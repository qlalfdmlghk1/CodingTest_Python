# import sys
# input = sys.stdin.readline
# from collections import deque
# n = int(input())
# dp = deque()
# dp.append(0)
# dp.append(1)
#
# while n > 1 :
#     dp.append((dp[0] + dp[1]) % 1000000007)
#     dp.popleft()
#     n -= 1
# print(dp[1])

N = int(input())
matrix = [[1, 1], [1, 0]]

# 행렬 곱셈
def mul_matrix(mat1, mat2):
    res = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for z in range(2):
                # c11 = a11*b11 + a12*b21
                res[i][j] += mat1[i][z] * mat2[z][j] % 1000000007
    return res

# 분할정복
def power(a, b):
    if b == 1:  # b의 값이 1이 될 때까지 재귀
        return a
    else:
        tmp = power(a, b // 2)  # a^(b // 2)
        if b % 2 == 0:
            return mul_matrix(tmp, tmp)  # b가 짝수인 경우
        else:
            return mul_matrix(mul_matrix(tmp, tmp), a)  # b가 홀수인 경우
result = power(matrix, N)

# 출력
print(result[0][1] % 1000000007)