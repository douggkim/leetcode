class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x:x[0])
        
        result_l = [intervals[0]]
        
        for gap in intervals[1:]: 
            if gap[0] <= result_l[-1][1]: 
                result_l[-1][1] = max(result_l[-1][1], gap[1] )
            else: 
                result_l.append(gap)
        
                
        return result_l