class Solution:
    def longestPalindrome(self, s: str) -> str:
        # odd 
        max_len = 0 
        longest_pal = "" 
        
        str_len = len(s)
        for i in range(str_len): 
            l = i 
            r = i 
            
            while l >= 0 and r < str_len: 
                if s[l] == s[r]: 
                    if max_len < r-l+1:
                        max_len = r-l+1
                        longest_pal = s[l:r+1]
                else: 
                    break 
                    
                l -= 1 
                r += 1 
            
        
        # even 
        
            l = i 
            r = i+1 
            
            while l >= 0 and r < str_len: 
                if s[l] == s[r]: 
                    if max_len < r-l+1: 
                        max_len = r-l+1 
                        longest_pal = s[l:r+1]
                    
                else: 
                    break 
                
                l -= 1 
                r += 1
        
        return longest_pal
        