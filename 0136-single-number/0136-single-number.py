class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once = set() 
        twice = set() 
    
        for i in nums: 
            if i in once: 
                twice.add(i)
            else: 
                once.add(i)
        
        return list(once-twice)[0]