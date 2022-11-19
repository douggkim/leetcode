class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [1,2]
        cases=[0]*(n+1)
        cases[0]=1 
        
        for i in range(1,len(cases)): 
            for step in steps:             
                if step <= i: 
                    cases[i] += cases[i-step]        
        return cases[n]
        