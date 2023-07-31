class Solution:
    def singleNumber(self, nums: List[int]) -> int: 
        result_d = set()  
        
        for n in nums: 
            if n in result_d: 
                result_d.remove(n)
            else: 
                result_d.add(n)
        
        return list(result_d)[0]