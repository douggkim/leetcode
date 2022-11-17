class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert to lower 
        s = s.lower() 
        # Remove all the other characters 
        convert_l = []
        for i in range(len(s)): 
            if ord('a')<=ord(s[i])<=ord('z') or s[i].isnumeric(): 
                convert_l.append(s[i])
        
        s=''.join(convert_l)
        print(s)
         
        if s == s[::-1]:
            return True
        else:
            return False
        # use [::-1]