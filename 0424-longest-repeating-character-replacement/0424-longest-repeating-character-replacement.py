class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result_dict = {} 
        max_cnt = 0 
        majority = 0 
        length = 0 
        
        # continue moving 
        for i,c in enumerate(s): 
            if c in result_dict: 
                result_dict[c] += 1
                
            else: 
                result_dict[c] = 1 
                
            if result_dict[c] >= majority: 
                    majority = result_dict[c]
                
            
            length += 1 

            remain = length - majority
            if remain <= k:
                max_cnt = length
            else: 
                result_dict[s[i-length+1]]-=1
                majority = max(result_dict.values())
                length -= 1
        
        return max_cnt
                
                
                
        
        # if break condition
        
        