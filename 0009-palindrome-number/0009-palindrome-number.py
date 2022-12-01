class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # input : always an integer 
        # EC : minus in front of the number
        # 1) turn to str 
        str_x = str(x)
        # 3) compare the reversed string  (EC#1)
        if str_x == str_x[::-1]: 
            return True 
        else:
            return False
    
        
        
        