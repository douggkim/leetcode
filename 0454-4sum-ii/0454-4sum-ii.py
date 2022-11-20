class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        result_dict = defaultdict(int)
        cnt = 0 
        n = len(nums1)
        
        for i in range(n):
            for j in range(n): 
                
                result_dict[nums1[i]+nums2[j]] += 1 
        
        for i in range(n):
            for j in range(n):
                
                cnt += result_dict[-(nums3[i]+nums4[j])]
                    
        return cnt 
                    