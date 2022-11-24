class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r = []
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] >0 : 
                break 
            if i == 0 or nums[i-1] != nums[i]:
                self.twosum(nums, i, r)
        return r 
        
    def twosum(self, nums,start,r): 
        result = set() 
        i = start+1
        while i < len(nums):
            tmp = nums[start] + nums[i]
            if -1*tmp in result: 
                r.append([nums[i],nums[start],-1*tmp])
                while i +1 < len(nums) and nums[i] == nums[i+1]:
                    i += 1 

            result.add(nums[i])
            i+=1
                
                    
                
                
        
            
        
        return r
                        
                
        