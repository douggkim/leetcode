class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        steps = [1,2]
        # EC : 0 length 
        # EC : 1 length 
        
        # Start from 0 
        rec = [0]*(len(cost)+1) 
        for i in range(1, len(cost)+1): 
            if i == 1:
                rec[i] += cost[i-1]
            else:
                rec[i] = min(rec[i-1]+cost[i-1],rec[i-2]+cost[i-2])
        tmp1 = rec[len(cost)]
        print(rec)
        
        rec = [0]*(len(cost)+1)
        for i in range(2,len(cost)+1):
            if i == 2: 
                rec[i]+=cost[i-1]
            else: 
                rec[i] = min(rec[i-1]+cost[i-1], rec[i-2]+cost[i-2])
        tmp2 = rec[len(cost)]
        print(rec)
        
        return min(tmp1,tmp2)
            

    # start from 1