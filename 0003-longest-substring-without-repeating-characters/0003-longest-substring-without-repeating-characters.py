class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = "" 
        max_len = 0 
        
        for c in s: 
            if c not in ss: 
                ss += c
            else:
                idx = ss.index(c)
                
                if idx+1 <= len(ss)-1:
                    ss = ss[idx+1:] + c
                else: 
                    ss = c
            
            
            max_len = max(max_len, len(ss))
        
        return max_len