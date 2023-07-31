class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = math.inf 
        max_profit = -math.inf 

        for p in prices: 
            if p <= min_p: 
                min_p = p 
            
            tmp_profit = p - min_p

            if tmp_profit >= max_profit: 
                max_profit = tmp_profit 
        
        if max_profit < 0: 
            return 0 
        else:
            return max_profit

        