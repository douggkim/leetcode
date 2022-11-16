class Solution:
    def mySqrt(self, x: int) -> int:

        # binary search 
        l = 0 
        u = x
        
        while l<= u: 
            m = (l+u)//2
            if m*m == x: 
                return m 
            elif m*m < x < (m+1)*(m+1): 
                return m
            elif m*m < x : 
                l = m+1 
                
            else: 
                u = m-1
                
                    
        
        
        # # Brute force 
        # for i in range(0,x+1): 
        #     if i*i==x: 
        #         return i
        #     elif i*i>x: 
        #         return i-1
        #     else: 
        #         continue