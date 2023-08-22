class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        record_l = [0]*n
        result_l = [] 
        
        def dfs(tmp_l, record_l, total): 
            if total == n:
                result_l.append(tmp_l)
            if total > n:
                return 
            
            for i,v in enumerate(record_l): 
                if v == 0: 
                    tmp = record_l.copy()
                    tmp[i] = 1 
                    dfs(tmp_l+[nums[i]], tmp, total+1)
        
        dfs([],record_l,0)
        
        return result_l
                
            