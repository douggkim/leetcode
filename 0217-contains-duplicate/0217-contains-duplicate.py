class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0 :
            return False 
        result_dict = {}
        
        for i in range(len(nums)): 
            if nums[i] not in result_dict: 
                result_dict[nums[i]] = 1 
            else: 
                return True
        
        return False