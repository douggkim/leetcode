class Solution:
    def hammingWeight(self, n: int) -> int:
        # while  
        tmp = n 
        tot = 0 
        while tmp>1: 
            tot += (tmp %2) 
            tmp //=2
        
        if tmp == 1 : 
            tot += 1 
        
        return tot
        
        
        