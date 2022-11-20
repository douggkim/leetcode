class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) ==0 : 
            return []
        
        result_dict = {}
        
        for i in range(len(nums)): 
            if nums[i] in result_dict: 
                return [result_dict[nums[i]], i]
            else: 
                result_dict[target-nums[i]] = i
        
        return []
        