class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # Use a~z string to find the number
        ref = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # Create dict for numbers 
        let_dict = {}
        
        # Create a dict so we can refer to the numbers
        for i in range(len(ref)): 
            let_dict[ref[i]] = i+1
        
        
        # Total to record the sum of digits
        tot = 0 
        # add each digit as digits of 26
        for i in range(len(columnTitle)-1,-1,-1): 
            tot += (let_dict[columnTitle[i]]*(26**(len(columnTitle)-1-i)))
            
        return tot
            