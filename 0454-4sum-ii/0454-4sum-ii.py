class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        result_dict = {0:{},1:{},2:{},3:{}}
        nums = [nums1, nums2, nums3, nums4]
        n = len(nums1)
        
        for i in range(len(nums)): 
            for j in range(n): 
                if i == 0 : 
                    if nums[i][j] not in result_dict[i]: 
                        result_dict[i][nums[i][j]] = 1
                    else: 
                        result_dict[i][nums[i][j]] += 1
                elif i == 3 : 
                    if (-nums[i][j]) in result_dict[i-1]: 
                        if 0 in result_dict[i]: 
                            result_dict[i][0] += result_dict[i-1][-nums[i][j]]
                        else: 
                            result_dict[i][0] = result_dict[i-1][-nums[i][j]]
                else: 
                    
                    for k in result_dict[i-1].keys():
                        
                        if (k+nums[i][j]) not in result_dict[i]:
                            result_dict[i][k+nums[i][j]] = result_dict[i-1][k]
                        else: 
                            result_dict[i][k+nums[i][j]] += result_dict[i-1][k]

        if 0 in result_dict[3]:
            return result_dict[3][0]
        else: 
            return 0