class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted_s = ""
        
        for c in s: 
            lower_c = c.lower()
            if ('a' <= lower_c and lower_c <='z')  or lower_c.isnumeric(): 
                formatted_s += lower_c
                
        start = 0 
        end = len(formatted_s)-1 
        
        while start <= end: 
            if formatted_s[start] != formatted_s[end]: 
                return False 
            else: 
                start += 1 
                end -= 1 
                
        return True
        