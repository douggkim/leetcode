class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        rec_max = [0]*len(nums)
        rec_min = [0]*len(nums)
        rec_max[0] = rec_min[0] = nums[0]
        
        largest = rec_max[0]
        
        for i in range(1,len(nums)): 
            rec_max[i] = max(nums[i], nums[i]*rec_max[i-1],nums[i]*rec_min[i-1] )
            rec_min[i] = min(nums[i], nums[i]*rec_min[i-1], nums[i]*rec_max[i-1])
            
            if largest <= rec_max[i]: 
                largest = rec_max[i]
        
        
        return largest
                
        