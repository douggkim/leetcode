class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        record_l = [False] * len(s)
        
        for i, c in enumerate(s): 
            for word in wordDict: 
                if i < len(word)-1: 
                    continue 
                
                if i == len(word)-1 or record_l[i-len(word)]==True: 
                    if s[i-len(word)+1:i+1] == word: 
                        record_l[i] = True 
                        break 
        
        return record_l[-1]
            
        