class Solution:
    def countSubstrings(self, s: str) -> int:
        num = 0 
        s_len = len(s)-1 

        for i,c in enumerate(s): 
            #odd 
            l, r = i, i 

            while l >=0 and r <= s_len: 
                if s[l] == s[r]: 
                    num += 1
                else: 
                    break 
                l -= 1 
                r += 1 


            # even 
            l, r = i, i+1 

            while l >= 0 and r <= s_len: 
                if s[l] == s[r]: 
                    num += 1 
                else: 
                    break 
                
                l -= 1 
                r += 1 
                
        return num 
