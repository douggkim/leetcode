class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        tmp_total = sum(nums[0:k]) 
        max_avg = tmp_total/k 
        
        for i in range(1, len(nums)-k+1): 
            tmp_total = tmp_total - nums[i-1] + nums[i+k-1]
            max_avg = max(max_avg, tmp_total/k)
        
        return max_avg
        