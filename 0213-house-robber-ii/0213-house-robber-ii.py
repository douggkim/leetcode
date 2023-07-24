class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1: 
            return nums[0] 
        elif len(nums) == 2: 
            return max(nums[0], nums[1])
        record = []
        record.append([0]*len(nums))
        record.append([0]*len(nums)) 

        record[1][0] = nums[0]
        record[0][1] = nums[1]
        max_val = max(record[1][0],record[0][1])
        
        if len(nums) == 3: 
            record[0][2] = max(nums[1],nums[2])
            record[1][2] = record[1][0]
            return max(record[0][2], record[1][2])
        else: 
            record[0][2] = max(record[0][1], nums[2])
            record[1][2] = record[1][0]+nums[2]
            max_val = max(max_val, record[0][2])
            max_val = max(max_val, record[1][2])
        
        for i in range(3, len(nums)): 
            record[0][i] = max(nums[i]+record[0][i-2], nums[i]+record[0][i-3])
            if i != len(nums)-1: 
                record[1][i] = max(nums[i]+record[1][i-2], nums[i]+record[1][i-3])
            max_val = max(record[0][i],max_val)
            max_val = max(record[1][i],max_val)
        
        
        return max_val
        