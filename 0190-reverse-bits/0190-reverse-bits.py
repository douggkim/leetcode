class Solution:
    def reverseBits(self, n: int) -> int:
        tmp_n = n 
        bits = ""
        
        while tmp_n >= 1: 
            bits += str(tmp_n % 2)
            tmp_n //= 2 
            
        zero_nums = 32-len(bits)
        bits = bits + "0"*zero_nums
        
        result = 0 
        for i in range(0,len(bits)): 
            result += int(bits[i])*(2**(31-i))
        
        return result 
            