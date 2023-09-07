class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        if s1_len > s2_len: 
            return False 
        # Create permutation dictionary 
        permute_dict = {} 
        for c in s1: 
            permute_dict[c] = permute_dict.get(c,0)+1
        
        window_dict = {} 
        for i in range(0,s2_len-s1_len+1): 
            if i == 0: 
                for j in range(0,s1_len): 
                    window_dict[s2[j]] = window_dict.get(s2[j],0)+1 
            else:
                window_dict[s2[i-1]] -= 1 
                window_dict[s2[i+s1_len-1]] = window_dict.get(s2[i+s1_len-1],0)+1 
            
            
            is_found = True
            
            for k,v in window_dict.items(): 
                if window_dict[k] != 0: 
                    if permute_dict.get(k,0) == 0 or permute_dict[k] != v: 
                        is_found = False
                        break 
            
            if is_found == True: 
                return is_found 
        
        return False
                    
                    
        
        