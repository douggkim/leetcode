class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_vol = 0
        l = 0 
        r = len(height)-1
        while l < r: 
            width = r-l 
            if height[l]<=height[r]:
                min_idx = l 
                l += 1
            else:
                min_idx = r 
                r -= 1 
            vol = width*height[min_idx]
            if vol > max_vol:
                max_vol = vol 
            
                    
        return max_vol