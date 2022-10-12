class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        check_list = [0]*(10**4+1)
        num_len = len(nums)
        
        for num in nums: 
            check_list[num]+=1
            if check_list[num] >= num_len/2: 
                return num