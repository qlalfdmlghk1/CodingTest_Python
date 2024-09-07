nums = [7,7,7,7,7,7,7]
n = len(nums)
dp = [1] * n

for i in range(len(nums)) :
    for j in range(i) :
        if nums[j] < nums[i] :
            dp[i] = max(dp[j] + 1,dp[i])

print(dp)
print(max(dp))