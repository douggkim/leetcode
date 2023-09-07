class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0] 
        
        length = len(nums)
        if nums[0] < nums[length-1]: 
            return nums[0]
        
        start = 0 
        end = length-1 
        
        while start<end: 
            mid = (start+end)//2 
            
            if nums[mid] < nums[mid-1]: 
                return nums[mid]
            elif nums[mid] > nums[mid+1]: 
                return nums[mid+1]
            
            if nums[mid] > nums[start]: 
                start = mid +1 
            else: 
                end = mid
        