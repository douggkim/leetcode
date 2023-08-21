class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result_l = [] 
        
        def dfs(curr_set, nums, max_idx, result_l, flag)-> List[List[int]]: 
            if max_idx < -1: 
                return result_l
            if flag == 0: 
                result_l.append(curr_set)
            new_curr_set = curr_set.copy()
            result_l = dfs(new_curr_set, nums,max_idx-1, result_l, 1)
            
            new_curr_set.append(nums[max_idx])
            new_curr_set_2 = new_curr_set.copy()
            result_l = dfs(new_curr_set_2, nums,max_idx-1, result_l, 0)
            
            return result_l
        
        result_l = dfs([],nums,len(nums)-1, result_l, 0)
        
        return result_l