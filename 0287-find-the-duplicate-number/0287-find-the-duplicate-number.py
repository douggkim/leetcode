class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        result_dict = {} 
        
        for n in nums: 
            if n in result_dict: 
                return n 
            else: 
                result_dict[n]=1 
        
        