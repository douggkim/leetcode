class Solution:
    def findTargetSumWays(self, nums, S):
        total = sum(nums)
        dp = [[0]*(2*total+1) for _ in range(len(nums))]
        
        dp[0][total+nums[0]] = 1 
        dp[0][total-nums[0]] += 1 
        
        for i in range(1,len(nums)): 
            for j in range(-total, total+1): 
                if dp[i-1][total+j] >0: 
                    dp[i][total+j+nums[i]] += dp[i-1][total+j]
                    dp[i][total+j-nums[i]] += dp[i-1][total+j]
        
        
        return 0 if abs(S) >total else dp[len(nums)-1][total+S]