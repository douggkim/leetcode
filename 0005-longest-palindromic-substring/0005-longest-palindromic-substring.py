class Solution:
    def longestPalindrome(self, s: str) -> str:
        # EC : even length palindrome 
        # loop throuh the chracter
        maxlen = 1 
        result_s = ""
        
        for i in range(len(s)): 
            l = i 
            r = i 
            
            
            while l>-1 and r < len(s):
                if s[l] == s[r]: 
                    if r-l+1 >= maxlen:
                        maxlen = r-l+1 
                        result_s = s[l:r+1]
                    l -= 1
                    r += 1 
                else: 
                    break
                
            
            l = i
            r = i+1 
            
            while l>-1 and r < len(s):
                if s[l] == s[r]: 
                    if r-l+1 >= maxlen:
                        maxlen = r-l+1 
                        result_s = s[l:r+1]
                    l -= 1
                    r += 1
                else: 
                    break 
                    
        return result_s
        