class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#         Diff length
        if len(s)!= len(t):
            return False 
        # 0 length 
        if len(s) == 0: 
            return True 
        
        result_dict = {} 
        # Initiate the keys 
        for letter in 'abcdefghijklmnopqrstuvwxyz': 
            result_dict[letter] = 0 
            
        # Run through s and get the numbers 
        for i in range(len(s)): 
            result_dict[s[i]] += 1 
            
        for j in range(len(t)): 
            result_dict[t[j]] -= 1 
            
        for ele in result_dict: 
            if result_dict[ele] != 0: 
                return False
        
        return True
        # Run through t and subtract the numbers 
        # see if everything is 0 
        