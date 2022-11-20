class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        result_dict = {} 
        cnt = 0 
        n = len(nums1)
        
        for i in range(n):
            for j in range(n): 
                if (nums1[i]+nums2[j]) not in result_dict: 
                    result_dict[nums1[i]+nums2[j]] = 1
                else: 
                    result_dict[nums1[i]+nums2[j]] += 1 
        
        for i in range(n):
            for j in range(n):
                if -(nums3[i]+nums4[j]) in result_dict: 
                    cnt += result_dict[-(nums3[i]+nums4[j])]
                    
        return cnt 
                    