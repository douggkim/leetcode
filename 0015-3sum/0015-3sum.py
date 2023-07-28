class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        i = 0
        result_l = [] 
        while i < len(sorted_nums): 
            if sorted_nums[i] > 0: 
                break
            if  i ==0 or sorted_nums[i] != sorted_nums[i-1]: 
                result_l = self.twoSum(sorted_nums[i:], result_l)
            i += 1 
        
        return result_l 
                
        
    def twoSum(self, nums: List[int], result_l: List[List[int]]) -> List[List[int]]: 
        fixed_num = nums[0]
        
        i = 1
        save = set()

        while i < len(nums):
            tmp_sum = nums[i] + fixed_num 
            if -tmp_sum in save: 
                result_l.append([nums[i], fixed_num, -tmp_sum])
                while i < len(nums)-1 and nums[i] == nums[i+1]:
                        i += 1 
            
            save.add(nums[i])
            i += 1 
            
        return result_l 
            
            
                 
                    
                