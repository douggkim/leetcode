class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        record_l = [0] * (len(cost)+1)
        
        for i in range(2,len(record_l)): 
            tmp_result_1 = record_l[i-2] + cost[i-2]
            tmp_result_2 = record_l[i-1] + cost[i-1]
            record_l[i] = min(tmp_result_1, tmp_result_2)
        
        return record_l[len(cost)]