from collections import defaultdict
nums = [5,4,-1,7,8] # output = 6
n = len(nums)
dp = nums
for i in range(1,n) :
    if dp[i-1] < 0 :
        dp[i] = nums[i]
    else :
        dp[i] = dp[i-1] + nums[i]
print(dp)
print(max(dp))


