class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Use ordered_dict 
        
        if len(nums) == 0: 
            return 0 
        
        # nums = list(set(nums)) 
        nums_s = set(nums)
        max_cnt = 1
        for i in range(len(nums)): 
            if nums[i]-1 in nums_s: 
                continue 
            else: 
                cnt = 1
                start = nums[i]+1
                while start in nums_s: 
                    cnt += 1 
                    start += 1 
                    max_cnt = max(max_cnt, cnt)
        
        

        return max_cnt
                
            
                
            
            
        # to list 