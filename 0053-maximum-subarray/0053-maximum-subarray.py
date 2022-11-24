class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        rec = [0]*len(nums)
        #Starting point 
        rec[0] = nums[0]
        largest = rec[0]
        
        for i in range(1, len(nums)): 
            rec[i] = max(nums[i],rec[i-1]+nums[i])
            if rec[i] > largest: 
                largest = rec[i]
                
        
        return largest 
                
        