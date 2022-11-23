class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0: 
            return False
        n_s = set(nums)
        return not(len(n_s)==len(nums))