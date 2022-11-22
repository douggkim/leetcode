class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals 
        intervals.sort(key=lambda x:x[0])
        # define result_l  add element 0 to result_l 
        result_l = [intervals[0]]
        # Run through intervals 
        for interval in intervals: 
        # if interval[0] of intervals <= result_l[-1][1]
            if interval[0] <= result_l[-1][1]: 
                result_l[-1][1] = max(result_l[-1][1],interval[1])
        # else: result_l.append(interval)
            else: 
                result_l.append(interval)
        
        return result_l
        
        
        
        
        
        
        
            
        