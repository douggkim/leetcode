class Solution:
    def singleNumber(self, nums: List[int]) -> int: 
        expected_sum = sum(list(set(nums))) * 2        
        
        return expected_sum-sum(nums)
