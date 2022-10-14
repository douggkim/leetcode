class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-2,-1,-1):
            print(f"i:{i} / nums[i]:{nums[i]}")
            if nums[i]< nums[i+1]:
                min = 100000
                for j in range(i+1,len(nums)):
                    if nums[i]< nums[j]:
                        if min > nums[j]:
                            min = nums[j]
                            min_idx = j
                temp = nums[i]
                nums[i] = min
                nums[min_idx] = temp
                nums[i+1:] = sorted(nums[i+1:])
                break
            
            if i == 0 : 
                nums.sort() 