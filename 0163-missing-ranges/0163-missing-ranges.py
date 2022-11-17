class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        # if lower == upper 
        if lower==upper: 
            if lower in nums:
                return []
            else: 
                return [str(lower)]
        if len(nums)==0: 
            if lower != upper: 
                return [str(lower)+"->"+str(upper)]
        # List to store results 
        result_l = []
        tmp_l = lower 
        
        for i in range(len(nums)): 
            if tmp_l < nums[i]:
                if tmp_l + 1 == nums[i]: 
                    result_l.append(str(tmp_l))
                else:
                    result_l.append(str(tmp_l)+"->"+str(nums[i]-1))
            tmp_l = nums[i]+1 
        
        if tmp_l <= upper : 
            if tmp_l== upper: 
                result_l.append(str(tmp_l))
            else:
                result_l.append(str(tmp_l)+"->"+str(upper))
        
        return result_l
                    
            
            
            