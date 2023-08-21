class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result_l = [] 
        n = len(candidates)
        def dfs(curr_set, start, remainder): 
            if remainder == 0: 
                result_l.append(curr_set)
                return 
            
            elif remainder < 0: 
                return
                
            
            for i in range(start, n):
                flag = dfs(curr_set+[candidates[i]], i, remainder-candidates[i])
                
                
        
        
        dfs([],0, target)
        
        return result_l 
            