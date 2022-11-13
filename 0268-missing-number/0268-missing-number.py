class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        curr_sum = sum(nums) 
        target_sum = len(nums)*(len(nums)+1)/2
        return int(target_sum -curr_sum)