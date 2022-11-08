from copy import deepcopy
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        for i in range(length-1,-1,-1): 
            s.append(s[i])
            
        for i in range(length):
            s.pop(0)
        
            
        
        
        