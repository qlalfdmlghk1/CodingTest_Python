T = int(input())
for test_case in range(1, T + 1):
    #######################################################################################################
    from itertools import product

    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = product(arr, arr)
    arr = sorted(arr)

    for ind, arrays in enumerate(arr):
        print(ind+1, arrays)
        if (ind + 1) == k:
            result = sum(arrays)
    print(result)