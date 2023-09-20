class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr:List[int], start:int)->List[int]: 
            result_l.append(curr.copy())
             
            for i in range(start, n): 
                curr.append(nums[i])
                backtrack(curr, i+1)
                curr.pop()
        
        result_l = [] 
        n = len(nums)
        backtrack([],0)
        
        return result_l
            
