class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # loop from 1
        cnt = 0 
        i = 0 
        while i < len(nums): 
            if nums[i] == 0: 
                cnt+=1 
                nums.pop(i)
            else: 
                i +=1 
        
        zero_l = [0]*cnt
        nums.extend(zero_l)
                    
                
        # loop reverse till 1
        # if i != 0 switch with ==0 
        # if i == 0 skip 
        # if -1 < 0 switch 
        
        
        