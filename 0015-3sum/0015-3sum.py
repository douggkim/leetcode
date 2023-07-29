class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_num = sorted(nums) 
        result_l = [] 
        
        for i in range(len(sorted_num)): 
            if sorted_num[i] > 0:
                break 
            if i==0 or sorted_num[i]!= sorted_num[i-1]: 
                result_l = self.twoSum(sorted_num[i:], result_l)
        
        return result_l 
        
    def twoSum(self, nums: List[int], result_l: List[List[int]]) -> List[List[int]]: 
        start = nums[0]
        
        i = 1
        visited = set() 
        while i < len(nums): 
            tmp_val = nums[i] + start 
            if -tmp_val in visited: 
                result_l.append([start, nums[i], -tmp_val])
                while i < len(nums)-1 and nums[i] == nums[i+1]: 
                    i += 1 
            
            visited.add(nums[i])
            i += 1 
            
        return result_l 
        
        
            
                 
                    
                