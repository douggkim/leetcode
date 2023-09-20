class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0 
        zero_cnt = 0 
        
        while i < len(nums): 
            if nums[i] == 0: 
                nums.pop(i)
                zero_cnt += 1 
            else: 
                i += 1 
                
        nums.extend([0]*zero_cnt)
        
        return nums 