class Solution:
    def reverseBits(self, n: int) -> int:
        tmp = n
        bin_str = ''
        # convert to 2 bits
        while tmp > 1 : 
            bin_str = bin_str + str(tmp%2)
            tmp //= 2
        
        if tmp == 1 : 
            bin_str = bin_str + '1'
        else: 
            bin_str = bin_str + '0'
            
        while len(bin_str) < 32: 
            bin_str = bin_str + '0'
        
        result = 0 
        for i in range(len(bin_str)-1,-1,-1): 
            result += (int(bin_str[i])*(2**(len(bin_str)-1-i)))
            
        return result
            
        
        # make it 32 bits length 
        # reverse the 2 bits string
        # convert the rev string to int
        