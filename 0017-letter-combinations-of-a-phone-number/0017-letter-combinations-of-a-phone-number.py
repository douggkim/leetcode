class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0 : 
            return [] 
        number_dict = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h", "i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]
        }
        
        n = len(digits)
        result_l = []
        
        def backtrack(start:int, tmp:str):
            if start >= n: 
                result_l.append(tmp)
                return 
            
            
            curr_digit = digits[start]
            letter_l = number_dict[curr_digit]
            for i in range(0, len(letter_l)): 
                backtrack(start+1, tmp+letter_l[i])
        
        backtrack(0,"")
        
        return result_l 
        
            
            