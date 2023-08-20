class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total % 2 != 0: 
            return False 
        
        subtotal = total //2 
        
        n = len(nums)
        
        @cache 
        def dfs(nums:tuple[int], n:int, subset_sum:int) -> bool: 
            if subset_sum == 0: 
                return True
            
            if n == 0 or subset_sum < 0 : 
                return False 
            
            return (dfs(nums, n-1, subset_sum-nums[n-1]) 
                   or dfs(nums, n-1, subset_sum)) 
        
        return dfs(tuple(nums), n-1, subtotal)