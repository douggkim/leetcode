class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]
        nums_len = len(nums)
        if nums[0] < nums[nums_len-1]:
            return nums[0]
        
        l = 0 
        r = nums_len-1 
        
        while l < r: 
            mid = (l+r)//2 
            
            if nums[mid] <nums[mid-1]: 
                return nums[mid]
            elif nums[mid] > nums[mid+1]: 
                return nums[mid+1]
            
            if nums[mid] > nums[l]: 
                l = mid+1 
            else: 
                r = mid - 1 
        