class Solution:
    def rob(self, nums: List[int]) -> int:
        # Create a memo  - deep copy the list 
        memo = nums.copy() 
        # Use Memo as starting point / nums as adding numbers 
        # EC 1: if len(nums)<2 
        if len(nums)<2: 
            return max(nums)
        
        for i in range(0,len(memo)-2):
            for j in range(i+2,len(nums)): 
                memo[j] = max(memo[i]+nums[j],memo[j])
        
        return max(memo)
                
        # for each memo[i]  loop with nums[i+2]
        # ec #1 : if nums =[]
        # ec #2 : if len(nums) == 1 