class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) <= len(str2): 
            start_str = str1
        else: 
            start_str = str2
        
        answ = "" 
            
        for i in range(len(start_str)): 
            if len(str1) % (i+1) == 0 and len(str2)%(i+1)==0: 
                common_str = start_str[0:i+1]
                # print(common_str)
                is_invalid = False 
                # print(i+1)
                for j in range(0,len(str1),i+1): 
                    # print(f"{j}/{len(str1)}")
                    if str1[j:j+i+1] != common_str: 
                        # print("invalid")
                        is_invalid = True 
                        break
                if is_invalid: 
                    continue
                # print("first string passed")
                for j in range(0,len(str2),i+1): 
                    # print(str2[j:j+i+1])
                    if str2[j:j+i+1] != common_str: 
                        is_invalid = True 
                        break
                
                if is_invalid: 
                    continue 
                answ = common_str            
            
            else: 
                continue
                
        return answ
        
        
        