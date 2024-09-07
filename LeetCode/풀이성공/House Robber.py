from collections import defaultdict
nums = [0]
n = len(nums)
dp = {}
for i in range(n) :
    dp[i] = nums[i]

for i in range(2,n) :
    if i == 2 :
        dp[i] = nums[0] + nums[i]
    else :
        dp[i] = max(dp[i-2] + nums[i], dp[i-3] + nums[i])
print(max(dp.values()))
print(dp)