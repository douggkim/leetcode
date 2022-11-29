class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # EC : minus 
        # check minus 
        neg = False
        if x<0: 
            neg = True 
            x = x*-1 
        str_x = str(x) 
        # to string & reverse the string 
        new_str = str_x[::-1]
        new_int = int(new_str)
        if neg: 
            new_int = new_int * -1 
        
        # Check if -2**31  < < 2**31-1
        if new_int< -2**31 or new_int > 2**31-1:
            return 0 
        # if not return 0 
        else: 
            return new_int