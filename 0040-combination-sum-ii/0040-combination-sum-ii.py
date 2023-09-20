class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result_l = set()
        n = len(candidates)
        candidates.sort()

        def backtrack(tmp_t, start, remain): 
            if remain == 0: 
                result_l.add(tmp_t)
                return
            if remain < 0 or start==n: 
                return
            
            for i in range(start, n): 
                if i != start and candidates[i] == candidates[i-1]: 
                    continue  
                new_tuple = tmp_t+tuple([candidates[i]])
                backtrack(new_tuple, i+1, remain-candidates[i])
        
        backtrack((), 0, target)

        return list(result_l)

        