class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result_l = [False for _ in range(len(candies))]
        
        for i,c in enumerate(candies): 
            if c+extraCandies>=max_candies: 
                result_l[i] = True 
        
        return result_l 