class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # loop through the prices 
        # select a beg day 
        # select a end - day from beg+1 
        # subtract 
        # if larger than 0 
        # save results to a list 
        if len(prices) == 0: 
            return 0 
        
        min_price = 100000000
        max_prof = 0 
        
        for i in range(len(prices)): 
            if prices[i] < min_price: 
                min_price = prices[i]
            elif min_price < prices[i]:
                max_prof = max(prices[i]-min_price,max_prof) 
            
        return max_prof
    
        #Edge cases: 