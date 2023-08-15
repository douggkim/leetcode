class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        record_l = [amount+1] * (amount+1)
        record_l[0] = 0 
        
        for i in range(1, len(record_l)): 
            for c in coins: 
                if i-c >= 0: 
                    record_l[i] = min(record_l[i], record_l[i-c]+1)
                    
        if record_l[amount] == amount+1: 
            return -1 
        else: 
            return record_l[amount]
            
            
        