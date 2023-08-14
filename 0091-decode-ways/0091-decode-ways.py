class Solution:
    def numDecodings(self, s: str) -> int:
        record_l = [0]*len(s)
        # first character
        if s[0] != "0": 
            record_l[0] = 1 
            
        # second character 
        if len(s) >= 2: 
            if s[1] != "0": 
                record_l[1] += record_l[0]
            if s[:2][0] != "0" and 1<= int(s[:2]) and int(s[:2]) <= 26:
                record_l[1] += 1 
        
        for i in range(2, len(s)): 
            if s[i] != "0": 
                record_l[i] += record_l[i-1]
            if s[i-1] != "0" and 1<= int(s[i-1:i+1]) and int(s[i-1:i+1]) <= 26: 
                record_l[i] += record_l[i-2]
        
        return record_l[-1]
            