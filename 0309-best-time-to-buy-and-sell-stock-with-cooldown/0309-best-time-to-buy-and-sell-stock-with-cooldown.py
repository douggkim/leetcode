class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        
        if n == 1: 
            return 0 
        
        stock_y = [[0,0] for i in range(n)]
        stock_n = [[0,0] for j in range(n)]
        
        #initiate first values 
        stock_y[0] = [-prices[0], 0] 
        # Second day
        # When no stock
        if stock_n[0][0] >= stock_y[0][0] + prices[1]: 
            stock_n[1] = [stock_n[0][0],0]
        else:
            stock_n[1] = [stock_y[0][0]+prices[1],1]
        
        # When have stock 
        max_val = max(stock_n[0][0]-prices[1], stock_y[0][0])
        stock_y[1] = [max_val, 0]
            
            
        
    
        
        for i in range(2,n): 
            # To buy
            if stock_n[i-1][1] == 1:
                buy_after_two_days = stock_n[i-2][0] - prices[i]
                max_value = max(buy_after_two_days, stock_y[i-1][0])
                stock_y[i] = [max_value,0]
            else: 
                max_value = max(stock_n[i-1][0]-prices[i], stock_y[i-1][0])
                stock_y[i] = [max_value,0]
            
            # To sell
            # NOt having anything in the first place 
            if stock_n[i-1][0] >= stock_y[i-1][0]+prices[i]: 
                max_value = stock_n[i-1][0]
                stock_n[i] = [max_value, 0]
            else: 
                max_value = stock_y[i-1][0]+prices[i]
                stock_n[i] = [max_value, 1]
                
        # print(stock_n)
        # print(stock_y)
                
        return max(stock_n[n-1][0], stock_y[n-1][0])
                
                