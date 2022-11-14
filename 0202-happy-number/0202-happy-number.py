class Solution:
    def isHappy(self, n: int) -> bool:
        # result_dict to check duplicacy 
        # repeat the addition 
        result_dict = {}
        
        while n not in result_dict: 
            result_dict[n]=1 
            str_n = str(n)
            tot_n = 0
            for i in range(len(str_n)): 
                tot_n += int(str_n[i])**2
            
            n = tot_n
            
            if tot_n == 1 : 
                return True 
        
        return False