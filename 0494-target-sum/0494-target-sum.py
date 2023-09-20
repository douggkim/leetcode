class Solution:
    def findTargetSumWays(self, nums, S):
        total = sum(nums)
        dp = [[0] * (2 * total + 1) for _ in range(len(nums))]
        dp[0][nums[0] + total] = 1
        dp[0][-nums[0] + total] += 1

        for i in range(1, len(nums)):
            for _sum in range(-total, total + 1):
                if dp[i - 1][_sum + total] > 0:
                    dp[i][_sum + nums[i] + total] += dp[i - 1][_sum + total]
                    dp[i][_sum - nums[i] + total] += dp[i - 1][_sum + total]

        return 0 if abs(S) > total else dp[len(nums) - 1][S + total]
