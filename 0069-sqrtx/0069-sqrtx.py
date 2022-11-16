class Solution:
    def mySqrt(self, x: int) -> int:
        # Brute force 
        for i in range(0,x+1): 
            if i*i==x: 
                return i
            elif i*i>x: 
                return i-1
            else: 
                continue

        # binary
#         if x == 0: 
#             return 0 
#         elif x == 1: 
#             return 1
#         else: 
#             tmp = x 
#             while tmp >= 0 : 
#                 if tmp**2 == x: 
#                     return tmp 
#                 elif tmp**2 > x:
                    
        
        
        # try x//2
        # if smaller? 
        # if larger? 
        
        # memoization