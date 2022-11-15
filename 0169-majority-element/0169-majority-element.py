class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # record number of occurences in dict 
        result_dict = {} 
        maj_num = (len(nums)//2)+1
        for i in range(len(nums)): 
            if nums[i] in result_dict: 
                result_dict[nums[i]] += 1 
                # if the recorded number is larger than majority return the number
                if result_dict[nums[i]]>= maj_num: 
                    return nums[i]
            else: 
                result_dict[nums[i]] = 1 
                if result_dict[nums[i]]>= maj_num: 
                    return nums[i]
                
        