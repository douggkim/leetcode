class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        record_l = [1] * len(nums)
        max_val = 1
        
        for i in range(len(nums)): 
            for j in range(i): 
                if nums[i] > nums[j]: 
                    record_l[i] = max(record_l[i], record_l[j]+1)
                    max_val = max(record_l[i], max_val) 
                    
                    
        
        return max_val
                        