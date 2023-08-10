class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0] 
        
        if nums[0] < nums[len(nums)-1]:
            return nums[0]
        
        l = 0 
        r = len(nums)-1 
        
        while l < r: 
            mid = (l+r)//2 
            
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[mid] < nums[mid-1]: 
                return nums[mid]
            else: 
                if nums[mid] < nums[l]: 
                    r = mid-1 
                else: 
                    l = mid+1
                    
        