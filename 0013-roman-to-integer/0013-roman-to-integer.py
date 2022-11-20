class Solution:
    def romanToInt(self, s: str) -> int:
        i = 0 
        sum = 0
        while i < len(s): 
            # print(f"i : {i}")
            # print(s[i])
            if s[i] == "I" :
                if i+1 < len(s): 
                    if s[i+1] == "V":
                        sum += 4
                        i += 2
                        continue

                    elif s[i+1] == "X":
                        sum += 9 
                        i += 2
                        continue
                
                
                sum += 1 
                # print(f"sum {sum} / i {i}" )

            elif s[i] == "X" :
                if i+1 < len(s): 
                    if s[i+1] == "L" :
                        sum += 40
                        i += 2
                        continue

                    elif s[i+1] == "C":
                        sum += 90
                        i += 2
                        continue
                
                
                sum += 10
            
            elif s[i] == "C" :
                if i+1 < len(s): 
                    if s[i+1] == "D":
                        sum += 400
                        i += 2
                        continue

                    elif s[i+1] == "M" :
                        sum += 900
                        i += 2
                        continue

                
                sum += 100
            elif s[i] == "V":
                sum += 5 
            
            elif s[i] == "L":
                sum += 50 
            
            elif s[i] == "D":
                sum += 500 
            
            elif s[i] == "M":
                sum += 1000
            
            i+=1
        
        return sum 
                    
                    
            