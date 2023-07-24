class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = "" 
        max_len = 0 

        for c in s: 
            if c not in ss: 
                ss += c 
            else: 
                ss = ss[ss.index(c)+1:]+c
            
            max_len = max(len(ss),max_len)
        
        return max_len 