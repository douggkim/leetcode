class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        result_dict = {} 
        
        for n in arr: 
            result_dict[n] = result_dict.get(n,0) + 1
        
        
        cnt_set = set() 
        
        for k,v in result_dict.items(): 
            if v in cnt_set: 
                return False 
            else: 
                cnt_set.add(v)
        
        return True
            