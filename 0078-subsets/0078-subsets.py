class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(k, first=0, curr=[]): 
            if len(curr) == k: 
                result_l.append(curr[:])
                return 
            
            for i in range(first,n): 
                curr.append(nums[i])
                backtrack(k, i+1, curr)
                curr.pop()
                
        result_l = [] 
        n = len(nums)
        for j in range(n+1): 
            backtrack(k=j)
            
        return result_l 
            
        