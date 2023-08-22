class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set([()])
        n = len(nums) 
        nums.sort()
        
        def backtrack(tmp, start): 
            if start == n: 
                return 
            
            for i in range(start, n): 
                new_tuple = tuple(list(tmp)+[nums[i]])
                ans.add(new_tuple)
                backtrack(new_tuple,i+1)
        
        backtrack((), 0)
        
        return list(ans)